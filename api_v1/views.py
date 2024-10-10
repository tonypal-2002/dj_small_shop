from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from backend.models import Category
from .serializers import CategorySerializer
from .pagination import CustomPagination  # Import the custom pagination class

# Custom pagination class to handle Content-Range header
class CustomPagination(PageNumberPagination):
    page_size = 2  # Default number of items per page

    def get_paginated_response(self, data):
        response = Response(data)
        total_items = self.page.paginator.count
        current_page = self.page.number
        response.headers['Content-Range'] = f'items {current_page}-{len(data)}/{total_items}'
        return response

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer