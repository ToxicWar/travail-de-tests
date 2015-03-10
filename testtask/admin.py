# coding: utf-8
from __future__ import unicode_literals
from django.contrib import admin
from .models import DynamicModel


admin.site.register([model for model in DynamicModel.registry.values()])
