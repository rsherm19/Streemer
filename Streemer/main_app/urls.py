from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.library, name='library'),
    path('playlists/', views.playlists, name='playlists'),
]
