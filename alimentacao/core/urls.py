# coding: utf-8
from django.conf.urls import include, url

from .views import MealCreateView, daily_report

urlpatterns = [
    url(r'^$', MealCreateView.as_view(), name='create'),
    url(r'^daily_report/$', daily_report, name='daily_report'),
]