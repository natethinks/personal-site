from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50)
    content = models.TextField()
    published = models.DateTimeField()
    slug = models.SlugField(max_length=100, unique=True)
	category = models.ForeignKey('blog.Category')

class Category(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
