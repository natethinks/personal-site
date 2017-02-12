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
	
	def get_context_data(self, **kwargs):
		context = dict()
		all_posts = Post.objects.all()
		context['post_list'] = all_posts.order_by('-published')
		return context
