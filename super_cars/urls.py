# coding: utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CarView.as_view(), name='index'),
    url(r'^ajax_api/(?P<manf>\w+)/$', views.ajax_api, name='ajax_api'),
]
