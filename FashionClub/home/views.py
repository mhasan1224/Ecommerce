#import email
#from tokenize import Name
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def shop(request):
    return render(request, 'shop.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def product_details(request):
    return render(request, 'product_details.html')


def blog(request):
    return render(request, 'blog.html')


def blog_single(request):
    return render(request, 'blog_single.html')


def contact_us(request):
    return render(request, 'contact_us.html')
