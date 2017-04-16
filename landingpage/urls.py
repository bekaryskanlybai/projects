from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^first/$', views.first_franchise, name='first_franchise'),
    url(r'^second/$', views.first_franchise, name='second_franchise'),
    url(r'^third/$', views.first_franchise, name='third_franchise'),
    url(r'^fourth/$', views.first_franchise, name='fourth_franchise'),
    url(r'^fifth/$', views.first_franchise, name='fifth_franchise'),
    url(r'^sixth/$', views.first_franchise, name='sixth_franchise'),
]
