
# Register your models here.
from django.contrib import admin
from .models import Competidor

@admin.register(Competidor)
class CompetidorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday', 'city', 'job')
    search_fields = ['first_name', 'last_name', 'city', 'job']
    list_filter = ['city', 'job']
    ordering = ['first_name']

