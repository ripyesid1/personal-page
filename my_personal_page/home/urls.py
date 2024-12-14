from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home_page'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('experience/', views.experience, name='experience'),
    path('comments/', views.comments, name='comments'),
]
