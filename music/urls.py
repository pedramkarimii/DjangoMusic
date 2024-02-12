# music/urls.py
from django.urls import path
from .views import MusicAddView, MusicInfoView, MusicDeleteView

urlpatterns = [
    path('add/', MusicAddView.as_view(), name='add'),
    path('info/', MusicInfoView.as_view(), name='info'),  # Add this line
    path('delete/<int:pk>/', MusicDeleteView.as_view(), name='delete'),
]