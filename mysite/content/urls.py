from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^learn/$', views.learn, name='learn'),
    url(r'^learn/(?P<lesson_id>[0-9]+)/$', views.lesson, name='lesson'),
    url(r'^learn/lists/$', views.word_list, name="Word Lists"),
    url(r'learn/lists/list_add/$', views.list_add, name="list_add"),
    # TODO: Need to check this and make the url equal to the list id or name.
    url(r'learn/lists/list_add/list_render/$', views.list_render, name='list_create'),
    ]
