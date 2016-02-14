# coding: utf-8
from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse

from .models import Meal


class MealCreateView(CreateView):
    model = Meal
    fields = ['is_good']

    def get_success_url(self):
        return reverse('core:daily_report')


def daily_report(request):
    return render(request, 'core/daily_report.html', {})

