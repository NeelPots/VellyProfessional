from django.contrib import admin
from django.urls import path, include
from vp import views

urlpatterns = [
   path('', views.index, name='home'),
   path('home', views.index, name='index'),
   path('about', views.about_us, name='about'),
   path('contact', views.contact, name='contact'),
   path('services', views.services, name='services'), 
]