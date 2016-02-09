# coding: utf-8
from django.conf.urls import include, url

from .views import MealCreateView

urlpatterns = [
    url(r'^$', MealCreateView.as_view(), name='create'),
]