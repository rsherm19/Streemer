from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.SignIn.as_view(), name='sign-in'),
    path('library/', views.library, name='library'),
    path('library/<int:song_id>', views.song_detail),
    path('playlists/', views.playlists, name='playlists'),
    path('playlists/<int:playlist_id>', views.playlist_detail),
]
