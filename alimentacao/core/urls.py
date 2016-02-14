# coding: utf-8
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.MealCreateView.as_view(), name='create'),
    url(r'^daily_report/$', views.daily_report, name='daily_report'),
]