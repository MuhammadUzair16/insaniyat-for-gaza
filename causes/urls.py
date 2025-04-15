from django.urls import path
from . import views

app_name = 'causes'

urlpatterns = [
    path('causes/', views.cause_list, name='cause_list'),
    path('causes/<slug:slug>/', views.cause_detail, name='cause_detail'),
]