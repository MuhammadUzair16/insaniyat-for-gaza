from django.contrib import admin
from .models import Volunteer

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submission_date', 'is_approved')
    list_filter = ('is_approved', 'submission_date')
    search_fields = ('name', 'email')
    list_editable = ('is_approved',)
    readonly_fields = ('submission_date',)