from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    # Set default page size
    page_size = 2  # Default number of items per page (you can modify it)

    # Allow the client to set the page size with a query parameter, if necessary
    page_size_query_param = 'perPage'

    # Set the maximum page size limit
    max_page_size = 100

    def get_paginated_response(self, data):
        """
        This method overrides the default pagination response to include custom headers.
        """
        total_items = self.page.paginator.count  # Total number of items
        current_page = self.page.number  # Current page number

        # Create the response with paginated data
        response = Response(data)

        # Set custom Content-Range header
        response.headers['Content-Range'] = f'items {current_page}-{len(data)}/{total_items}'

        return response
