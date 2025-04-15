from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_featured')
    list_filter = ('is_featured', 'date')
    search_fields = ('title', 'location', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'