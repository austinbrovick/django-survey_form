from django.conf.urls import patterns, url, include     # import functions to match patterns
from . import views                    # import views.py file from our quiz app
urlpatterns = patterns('',
  # this url pattern matches empty string!!!
  url(r'^$', views.index, name='index'),
  url(r'^survey/?$', views.process_form, name='process_form'),


)

