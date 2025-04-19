# boycott/urls.py
from django.urls import path
from .views import BoycottListView, BoycottDetailView, submit_report

app_name = 'boycott'

urlpatterns = [
    path('', BoycottListView.as_view(), name='boycott-list'),  # Changed from 'boycott/'
    path('category/<int:pk>/', BoycottListView.as_view(), name='boycott-category'),
    path('target/<int:pk>/', BoycottDetailView.as_view(), name='boycott-detail'),
    path('report/<int:pk>/', submit_report, name='submit-report'),
]