from django.conf.urls import url
from nate_travels.views import *
from . import views

app_name = 'nate_travels'
urlpatterns = [
    # ex: /home/
    url(r'^$', HomeView.as_view()),
]
#url(r'^$', views.index, name='index'),
