from django.contrib import admin
from .models import MyGraph

# Register your models here.

class MyGraphAdmin(admin.ModelAdmin):
    list_display = ('id', 'function_text', 'graph', 'interval', 'dt', 'date_modified')
    ordering = ('id',)

admin.site.register(MyGraph, MyGraphAdmin)