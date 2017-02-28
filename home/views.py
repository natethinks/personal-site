from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from home.models import Post, About
# Create your views here.

class AboutView(ListView):
	template_name = "home/about.html"
	model = About

	def get_context_data(self, **kwargs):
		context = dict()
		all_abouts = About.objects.all()
		context['about_list'] = all_abouts
		return context

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

def BlogDetailView(request, slug):
	post = Post.objects.get(slug = slug)
	context = { 'post': post }
	return render(request, "home/blogdetail.html", context)
