from django.contrib import admin
from .models import Project

@admin.register(Project)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'card_title', 'card_email')