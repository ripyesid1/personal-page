from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home_page'),
    path('home/about/', views.about, name='about'),
    path('home/services/', views.services, name='services'),
    path('home/experience/', views.experience, name='experience'),
    path('home/comments/', views.comments, name='comments'),
]
