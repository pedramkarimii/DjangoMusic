# music/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add, name="add"),
    path('delete/<int:music_id>/', views.delete, name="delete"),
    path('info/', views.info, name="info"),
]


