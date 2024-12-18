from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Comment, project, Blog_Post

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
    myprojects = project.objects.all().values()
    template = loader.get_template('works.html')
    context = {
        'myprojects' : myprojects,
    }
    return HttpResponse(template.render(context, request))

def blog(request):
    myposts = Blog_Post.objects.all().values()
    template = loader.get_template('blog.html')
    context = {
        'myposts' : myposts,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def blog_post(request, id):
    mypost = Blog_Post.objects.get(id=id)
    template = loader.get_template('blog_post.html')
    context = {
        'mypost' : mypost,
    }
    return HttpResponse(template.render(context, request))

def Project(request, id):
    myproject = project.objects.get(id=id)
    template = loader.get_template('project.html')
    context = {
        'myproject' : myproject,
    }
    return HttpResponse(template.render(context, request))
