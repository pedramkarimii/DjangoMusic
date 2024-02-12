# music/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('Main/', views.MusicInfoView.as_view(), name='Main'),
    path('add/', views.MusicAddView.as_view(), name='add'),
    path('info/', views.CountAllView.as_view(), name='info'),  # Add this line
    path('delete/<int:pk>/', views.MusicDeleteView.as_view(), name='delete'),
]
