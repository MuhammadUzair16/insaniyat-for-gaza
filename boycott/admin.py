from django.contrib import admin
from .models import BoycottCategory, BoycottTarget, UserReport, Alternative

@admin.register(BoycottCategory)
class BoycottCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)


@admin.register(Alternative)
class AlternativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name', 'description')




@admin.register(BoycottTarget)
class BoycottTargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'verified')
    list_filter = ('category', 'level', 'verified')
    filter_horizontal = ('alternatives',)
    search_fields = ('name', 'description')
    readonly_fields = ('last_updated',)

@admin.register(UserReport)
class UserReportAdmin(admin.ModelAdmin):
    list_display = ('target', 'submitted_by', 'date_submitted', 'approved')
    list_filter = ('approved', 'target__category')
    actions = ['approve_reports']

    def approve_reports(self, request, queryset):
        queryset.update(approved=True)
    approve_reports.short_description = "Approve selected reports"