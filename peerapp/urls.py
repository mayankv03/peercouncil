from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('services', views.services, name='services'),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('blog', views.blog, name='blog'),
    path('college', views.college, name='college'),
    path('testingonly', views.test, name='test'),
]