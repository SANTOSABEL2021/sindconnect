from django.contrib import admin
from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('socios/', views.socios, name='socios'),
    path('exemplos/', views.exemplos, name='exemplos'),
]