from django.contrib import admin
from django.urls import path, include
from .views import *

# http://127.0.0.1:8000/accounts/logout/
# http://127.0.0.1:8000/accounts/login/
urlpatterns = [
    path('accounts/login/', Login_Home.as_view(), name='Home_Login'),
    path('accounts/logout/', Log_Out.as_view(), name='Logout'),
    path('', Home.as_view(), name='Home'),
    path('accounts/profile/', Home.as_view(), name='Home'),
]
