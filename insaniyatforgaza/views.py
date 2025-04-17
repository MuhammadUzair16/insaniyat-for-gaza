from django.shortcuts import render
from about.models import AboutSection, Fact, TeamMember, Testimonial
from causes.models import Cause
from events.models import Event
from blog.models import BlogPost, Comment
from volunteer.models import Volunteer

def Home(request):
    context = {
        'about_section': AboutSection.objects.first(),
        'facts': Fact.objects.all().order_by('order'),
        'team_members': TeamMember.objects.all().order_by('order'),
        'testimonials': Testimonial.objects.all().order_by('order'),
        'causes': Cause.objects.all(),
        'events':Event.objects.all().order_by('date'),
        'blog_post':BlogPost.objects.all(),
        'comments':Comment.objects.all(),
        'volunteer': Volunteer.objects.all()

    }
    return render(request, 'home.html', context)

def service(request):
    context = {
        'causes': Cause.objects.all(),
    }
    return render(request, 'services.html', context)

def team(request):
    context = {
         'team_members': TeamMember.objects.all().order_by('order'),
    }
    return render(request, 'team.html', context)