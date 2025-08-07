from django.core.paginator import Paginator
from django.utils.functional import cached_property
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_page_size(self, request):
        page_size = int(
            request.query_params.get(self.page_size_query_param, self.page_size)
        )

        if page_size == 0:
            page_size = None

        return page_size


class FasterDjangoPaginator(Paginator):
    @cached_property
    def count(self):
        # only select 'id' for counting, much cheaper
        return self.object_list.values("id").count()


class CountFromExplainPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 1000
    django_paginator_class = FasterDjangoPaginator

    def get_page_size(self, request):
        page_size = int(
            request.query_params.get(self.page_size_query_param, self.page_size)
        )

        if page_size == 0:
            page_size = None

        return page_size


class NoCountPaginator(Paginator):
    @cached_property
    def count(self):
        return 9999999999


class NoCountPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    django_paginator_class = NoCountPaginator
