# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Customer

admin.site.register(Customer)
from django.contrib.auth.models import Service

admin.site.register(Service)