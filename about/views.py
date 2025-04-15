from django.shortcuts import render
from .models import AboutSection, AboutTab, Fact, TeamMember, Testimonial

def about_view(request):
    context = {
        'about_section': AboutSection.objects.first(),
        'facts': Fact.objects.all(),
        'team_members': TeamMember.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }
    return render(request, 'about/about.html', context)