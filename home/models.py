from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50, unique=True)
	author = models.CharField(max_length=50)
	content = models.TextField(help_text="<pre class='prettyprint'></pre>")
	published = models.DateTimeField()
	slug = models.SlugField(max_length=100, unique=True, blank=True)
	category = models.ForeignKey('home.Category')
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

class Category(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True, blank=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

class About(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True, blank=True)
	image_1 = models.URLField(blank=True)
	image_2 = models.URLField(blank=True)
	image_3 = models.URLField(blank=True)
	content = models.TextField()
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(About, self).save(*args, **kwargs)

class Project(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True, blank=True)
	image_1 = models.URLField(blank=True)
	image_2 = models.URLField(blank=True)
	image_3 = models.URLField(blank=True)
	content = models.TextField()

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Project, self).save(*args, **kwargs)
