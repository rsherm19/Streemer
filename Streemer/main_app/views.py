from django.shortcuts import render
from .models import Playlist, Song


def home(request):
    return render(request, 'home.html')


def playlists(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists.html', {'playlists': playlists})\

def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    songs = Song.objects.all()
    return render(request, 'playlist_detail.html', {
        'playlist': playlist,
        'songs': songs,
    })

def library(request):
    songs = Song.objects.all()
    return render(request, 'library.html', {'songs': songs})


def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'song_detail.html', {'song': song})