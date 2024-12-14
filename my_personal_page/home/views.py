from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Comment

def home_page(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def services(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())

def experience(request):
    template = loader.get_template('experience.html')
    return HttpResponse(template.render())

def comments(request):
    mycomments = Comment.objects.all().values()
    template = loader.get_template('comments.html')
    context = {
        'mycomments' : mycomments,
    }
    return HttpResponse(template.render(context, request))

def works(request):
    template = loader.get_template('works.html')
    return HttpResponse(template.render())

def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())