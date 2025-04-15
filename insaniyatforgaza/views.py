from django.shortcuts import render
from about.models import AboutSection, Fact, TeamMember, Testimonial
from causes.models import Cause
from events.models import Event
from blog.models import BlogPost, Comment

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

    }
    return render(request, 'home.html', context)