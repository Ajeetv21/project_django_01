from django.shortcuts import render
# myapp/views.py

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Create your views here.

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')  

def signup(request):
    return render(request,'signup.html')

def logout(request):
    return render(request,'logout.html')