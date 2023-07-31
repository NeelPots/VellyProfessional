from django.contrib import admin
from django.urls import path, include
from vp import views

urlpatterns = [
   path('', views.index, name='home'),
   path('home', views.index, name='index'),
   path('about', views.about_us, name='about'),
   path('contact', views.contact, name='contact'),
   path('services', views.services, name='services'), 
   path('packages', views.packages, name = 'packages'),
   path('career', views.career, name='career'),
   path('news', views.news, name='news'),
   path('footer', views.footer, name='footer'),
]