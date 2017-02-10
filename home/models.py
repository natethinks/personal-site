from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    published = models.DateTimeField()
    slug = models.SlugField()
