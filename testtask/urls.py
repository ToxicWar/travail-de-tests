# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('testtask.views',
    url(r'^$', 'testtask', name='TestTask'),
    url(r'^(?P<model_name>[\w]+)/$', 'model_data', name='ModelData'),
)
