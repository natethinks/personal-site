from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AboutView(TemplateView):
    template_name = "home/about.html"

class HomeView(TemplateView):
    template_name = "home/home.html"

class ContactView(TemplateView):
    template_name = "home/contact.html"

class PortfolioView(TemplateView):
    template_name = "home/portfolio.html"

class BlogView(TemplateView):
    template_name = "home/blog.html"
