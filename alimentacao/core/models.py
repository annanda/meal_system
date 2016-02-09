# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class Meal(models.Model):
    date = models.DateTimeField(_('Date'), auto_now=True, null=False, blank=True)
    is_good = models.BooleanField(_('Is Good?'), null=False, blank=True)

    def __str__(self):
        return '%s - %s' % (self.date, self.is_good)

    def get_absolute_url(self):
        return reverse('core:create')
