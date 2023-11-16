# myapp/urls.py
from django.urls import path
from .views import home, about,contact,login,logout,signup

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout,name='logout'),
]
