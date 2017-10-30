from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^learn/$', views.learn, name='learn'),
    url(r'^learn/(?P<lesson_id>[0-9]+)/$', views.lesson, name='lesson'),
    ]
