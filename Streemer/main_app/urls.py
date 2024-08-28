from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.SignIn.as_view(), name='sign-in'),
    path('accounts/signup', views.signup, name='sign-up'),
    path('library/', views.library, name='library'),
    path('library/<int:song_id>', views.song_detail),
    path('library/add/', views.CreateSong.as_view(), name='create-song'),
    path('library/<int:pk>/delete/', views.DeleteSong.as_view(), name='delete-song'),
    path('playlists/', views.playlists, name='playlists'),
    path('playlists/<int:playlist_id>', views.playlist_detail, name='playlist-detail'),
    path('playlists/create', views.CreatePlaylist.as_view(), name='create-playlist'),
    path('playlists/<int:pk>/update', views.UpdatePlaylist.as_view(), name='update-playlist'),
    path('playlists/<int:pk>/update-title', views.UpdatePlaylistTitle.as_view(), name='update-playlist-title'),
    path('playlists/<int:playlist_id>/remove-song/<int:song_id>', views.remove_song, name='remove-song'),
    path('playlists/<int:pk>/delete', views.DeletePlaylist.as_view(), name='delete-playlist'),
]
