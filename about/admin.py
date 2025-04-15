from django.contrib import admin
from .models import AboutSection, AboutTab, Fact, TeamMember, Testimonial

class AboutTabInline(admin.TabularInline):
    model = AboutTab
    extra = 1

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    inlines = [AboutTabInline]
    list_display = ('title', 'created_at')

@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ('label', 'count', 'is_money', 'order')
    list_editable = ('order',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')
    list_editable = ('order',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'order')
    list_editable = ('order',)