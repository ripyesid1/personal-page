from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home_page'),
    path('home/about/', views.about, name='about'),
    path('home/services/', views.services, name='services'),
    path('home/experience/', views.experience, name='experience'),
    path('home/works/', views.works, name='works'),
    path('home/blog/', views.blog, name='blog'),
    path('home/contact/', views.contact, name='contact'),
    path('home/comments/', views.comments, name='comments'),
    path('home/blog/<int:id>', views.blog_post, name='blog'),
    path('home/works/<int:id>', views.Project, name='project'),
]
