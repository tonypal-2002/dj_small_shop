from django.shortcuts import render

from backend.models import Product, Category


# Create your views here.
def home(request):
    context = {
        'categories': Category.objects.all(),
        'prouducts': Product.objects.all()
    }
    return render(request, 'frontend/home.html', context)

def forget_password(request):
    return render(request, 'frontend/forget_password.html')