from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from home.models import Post
# Create your views here.

class AboutView(TemplateView):
	template_name = "home/about.html"

class HomeView(TemplateView):
	template_name = "home/home.html"

class ContactView(TemplateView):
	template_name = "home/contact.html"

class PortfolioView(TemplateView):
	template_name = "home/portfolio.html"

class BlogListView(ListView):
	template_name = "home/blog.html"
	model = Post    
	
	ordered_posts = Post.objects.order_by('published')
	
	def get_context_data(self, **kwargs):
		context = Post.objects.order_by('published')
		return context
