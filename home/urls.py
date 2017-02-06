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
]
#url(r'^$', views.index, name='index'),
