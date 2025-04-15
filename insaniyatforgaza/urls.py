from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import about
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('about/', include('about.urls')),
    path('', include('causes.urls', namespace='causes')),
    path('', include('events.urls', namespace='events')),
    path('', include('blog.urls', namespace='blog')),
    path('contact/', include('contact.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
