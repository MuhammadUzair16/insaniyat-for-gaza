from django.urls import path
from . import views

app_name = 'volunteer'

urlpatterns = [
    path('volunteer/', views.volunteer_view, name='volunteer'),
]