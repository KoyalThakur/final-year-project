from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf.urls import url
from .views import PropertyAddView, PropertyListView

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('signIn',views.signin,name='signin'),
    path('searchResult',views.searchResult,name='searchResult'),
    url(r'^signUp/$', views.signup, name='signup'),
    path('listings', PropertyListView.as_view(), name='listings'),
    path('add', PropertyAddView.as_view(), name='add'),
    path('logout/', views.logout_view, name='logout')
]