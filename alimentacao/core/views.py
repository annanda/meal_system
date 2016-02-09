# coding: utf-8
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Meal


class MealCreateView(CreateView):
    model = Meal
    fields = ['is_good']


def daily_report(request):
    pass
