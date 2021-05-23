from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf.urls import url

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('signIn',views.signIn,name='signIn'),
    # path('signUp', views.signUphandle, name='signUphandle'),
    path('searchResult',views.searchResult,name='searchResult')
   
]