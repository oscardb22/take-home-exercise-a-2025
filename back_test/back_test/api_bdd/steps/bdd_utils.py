from types import NoneType

from dateutil import parser
from django.apps import apps
from jsonschema import Draft7Validator, validators

VALID_SCHEMA_TYPES = {
    "string": "string",
    "number": "number",
    "integer": "number",
    "datetime": "datetime",
}


def bulk_create_instances(context, model):
    """
    Creates multiple instances of a Django model from a table in the Behave context.

    Args:
        context (behave.Context): Behave context containing the data table.
        model (Model): Django model for which instances will be created.

    Returns:
        None: Instances are created and saved to the database.
    """
    instances = []
    for row in context.table:
        data = {heading: row[heading] for heading in row.headings}
        instances.append(model(**data))
    model.objects.bulk_create(instances)


def get_model_from_string(model_identifier):
    """
    Retrieves a Django model from a string in the format 'app_label.ModelName'.

    Args:
        model_identifier (str): String identifying
        the model in the format 'app_label.ModelName'.

    Returns:
        Model: The corresponding Django model.

    Raises:
        ValueError: If the format of `model_identifier` is invalid.
        LookupError: If the model is not found in the specified app.
    """
    try:
        app_label, model_name = model_identifier.split(".")
        return apps.get_model(app_label, model_name)
    except ValueError as e:
        raise ValueError(
            f"Invalid format for '{model_identifier}'. Use 'app_label.ModelName'"
        ) from e
    except LookupError as e:
        raise LookupError(
            f"Model '{model_identifier}' not found. "
            "Check the app_label and model_name."
        ) from e


def is_datetime(checker, obj):
    return bool(parser.parse(obj))


validator_datetime = validators.extend(
    Draft7Validator,
    type_checker=Draft7Validator.TYPE_CHECKER.redefine("datetime", is_datetime),
)


def validate_with_datetime(schema, instance):
    """
    custom validator to add datetime validation type
    """
    validator_datetime(schema=schema).validate(instance)


def convert_object_to_json_schema(obj, key=None):
    """
    Recursive function that will convert a Python object to a jsonschema object.
    Currently, it supports lists and dictionaries for the encapsulation,
    and the base objects int, str and None

    It has the special handling for string, starting with #, to define expected data:
        - string => string
        - number => number
        - datetime => datetime

    """
    expected_schema = {"properties": {}, "required": [], "additionalProperties": False}

    if isinstance(obj, list):
        expected_schema["type"] = "array"
        expected_schema["items"] = []
        if key:
            expected_schema["required"] = [key]
        for list_object in obj:
            list_obj_schema = convert_object_to_json_schema(list_object)
            expected_schema["items"].append(list_obj_schema)
    elif isinstance(obj, dict):
        expected_schema["type"] = "object"
        for _key, value in obj.items():
            dict_obj_schema = convert_object_to_json_schema(value, _key)
            if isinstance(value, dict):
                expected_schema["properties"][_key] = dict_obj_schema
            elif isinstance(value, list):
                expected_schema["properties"][_key] = dict_obj_schema
                expected_schema["required"] += dict_obj_schema["required"]
            else:
                expected_schema["properties"] |= dict_obj_schema["properties"]
                expected_schema["required"] += dict_obj_schema["required"]
    elif key and isinstance(obj, (str, int, NoneType)):
        if isinstance(obj, str) and obj.startswith("#"):
            data_type = obj[1:]
            expected_schema["properties"].update(
                {
                    key: {
                        "type": VALID_SCHEMA_TYPES[data_type],
                    }
                }
            )
        else:
            expected_schema["properties"].update({key: {"const": obj}})
        expected_schema["required"].append(key)
    return expected_schema
