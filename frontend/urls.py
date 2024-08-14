from django.urls import path

from frontend.views import forget_password, home

urlpatterns = [
    path('' , home),
    path('forget_password', forget_password),
]