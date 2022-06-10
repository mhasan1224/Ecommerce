#import email
#from tokenize import Name
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            first_name=fname, last_name=lname, email=email, username=username, password=password)
        user.save()
        return redirect('login/')
    return render(request, 'signup.html')