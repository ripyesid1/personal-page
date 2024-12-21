from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("userName", "firstName", "lastName")
class CommentAdmin(admin.ModelAdmin):
    list_display = ("userName", "comment")
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("projectName", "author", "summary")
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")

admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(project, ProjectAdmin)
admin.site.register(Blog_Post, BlogPostAdmin)