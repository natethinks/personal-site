from django.conf.urls import url
from home.views import *
from . import views


app_name = ''
urlpatterns = [
    # ex: /home/
	url(r'^$', HomeView.as_view()),
	url(r'^about$', AboutView.as_view()),
	url(r'^about/(?P<slug>[a-zA-Z0-9._-]+$)', views.AboutDetailView),
	url(r'^contact$', ContactView.as_view()),
	url(r'^portfolio$', PortfolioListView.as_view()),
	url(r'^portfolio/(?P<slug>[a-zA-Z0-9._-]+$)', views. PortfolioDetailView),
	url(r'^blog$', BlogListView.as_view()),
	url(r'^blog/(?P<slug>[a-zA-Z0-9._-]+$)', views.BlogDetailView)
]
#url(r'^$', views.index, name='index'),
