from django.shortcuts import render
from .models import Playlist, Song


def home(request):
    return render(request, 'home.html')


def playlists(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists.html', {'playlists': playlists})


def library(request):
    songs = Song.objects.all()
    return render(request, 'library.html', {'songs': songs})
