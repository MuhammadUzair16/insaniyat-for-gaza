from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from .views import Home, service, team

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('about/', include('about.urls')),
    path('', include('causes.urls', namespace='causes')),
    path('', include('events.urls', namespace='events')),
    path('', include('blog.urls', namespace='blog')),
    path('contact/', include('contact.urls')),
    path('', include('volunteer.urls', namespace='volunteer')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
