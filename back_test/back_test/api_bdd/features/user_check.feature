Feature: Check User

    Scenario: A login for user
        Given I create a superuser with email "admin@admin.com" and password "12346ASDFASDasdfa*" and UUID "7c4e6faf-62b0-4731-adf9-cd81c69cd7e0"
        When I make a POST request to "/api/auth/login/" with
        """
        {
            "email": "admin@admin.com",
            "password": "12346ASDFASDasdfa*"
        }
        """
        Then the response code is 200


    Scenario: A list of users
        Given I create a superuser with email "admin@admin.com" and password "12346ASDFASDasdfa*" and UUID "7c4e6faf-62b0-4731-adf9-cd81c69cd7e0"
        And I login with "admin@admin.com" and password "12346ASDFASDasdfa*"
        When I make a GET request to "/api/v1/authentication/users/"
        When the response code is 200
        Then the response "data" is equal to
        """
        {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{"groups": [],
                        "uuid": "7c4e6faf-62b0-4731-adf9-cd81c69cd7e0",
                        "email": "admin@admin.com",
                        "first_name": "",
                        "last_name": "",
                        "is_staff": True,
                        "is_active": True}]
        }
        """

    Scenario Outline: An existing user from "<domain>" should be accepted
        Given I create a user with email "<email>" and password "password"
        When I make a GET request to "/api/v1/authentication/email-check/?email=<email>"
        Then the response code is 200
        And the response "data" is equal to
        """
        {
        "count": 1,
           "next": None,
           "previous": None,
           "results": [{"groups": [],
                        "uuid": "7c4e6faf-62b0-4731-adf9-cd81c69cd7e0",
                        "email": "admin@admin.com",
                        "first_name": "",
                        "last_name": "",
                        "is_staff": True,
                        "is_active": True}]
        }
        """
        Examples:
            | email                 | domain           |
            | test@leangroup.com    | leangroup.com    |
            | test@lean-tech.io     | lean-tech.io     |
            | test@leanstaffing.com | leanstaffing.com |
