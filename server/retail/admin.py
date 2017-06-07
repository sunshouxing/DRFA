# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin

from .models import Chain, Store, Employee


# Register your models here.
@admin.register(Chain)
class ChainAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slogan', 'founded_date', 'website',)

    class Meta:
        model = Chain
        fields = '__all__'


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('chain', 'number', 'address', 'opening_date',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('store', 'number', 'first_name', 'last_name', 'hired_date',)

# EOF
