from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50)
    content = models.TextField()
    published = models.DateTimeField()
    slug = models.SlugField(max_length=100, unique=True)
	category = models.ForeignKey('blog.Category')
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

class Category(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)
