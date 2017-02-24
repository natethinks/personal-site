from django.conf.urls import url
from home.views import *
from . import views

app_name = ''
urlpatterns = [
    # ex: /home/
	url(r'^$', HomeView.as_view()),
	url(r'^about$', AboutView.as_view()),
	url(r'^contact$', ContactView.as_view()),
	url(r'^portfolio$', PortfolioView.as_view()),
	url(r'^blog$', BlogListView.as_view()),
	url(r'^blog/(?P<slug>[a-zA-Z])$', BlogDetailView.as_view(), name='blogdetail.html')
]
#url(r'^$', views.index, name='index'),
