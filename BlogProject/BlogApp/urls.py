from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('home', views.blogHome, name= 'Home'),
    path('contact', views.blogContact, name= 'contact'),
    path('about', views.blogAbout, name= 'about'),
    path('<str:slug>',views.blogPost, name = 'blogPost'),

]

