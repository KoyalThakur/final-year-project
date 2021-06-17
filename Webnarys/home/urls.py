from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('signIn',views.signin,name='signin'),
    path('searchResult',views.searchResult,name='searchResult'),
    url(r'^signUp/$', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('listings/', views.list_view, name='listings'),
    path('add/', views.add_property, name='add')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)