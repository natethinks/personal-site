from django.conf.urls import url

from . import views

app_name = ''
urlpatterns = [
    # ex: /home/
    url(r'^$', views.home,),
    url(r'^about$', views.about,),
    url(r'^contact$', views.contact,),
    url(r'^portfolio$', views.portfolio,),
]
#url(r'^$', views.index, name='index'),
