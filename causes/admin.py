from django.contrib import admin
from .models import Cause

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ('title', 'raised_amount', 'goal_amount', 'progress', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
