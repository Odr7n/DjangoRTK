from django.contrib import admin
from .models import *

# Register your models here.

class DashboardAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    list_filter = ['title', 'author', 'date']

admin.site.register(Dashboard, DashboardAdmin)