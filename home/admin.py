from django.contrib import admin

from .models import Post, Category, About, Project
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(About)
admin.site.register(Project)
