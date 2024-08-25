from django import views
from django.shortcuts import render
from .models import Playlist, Song
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')


class SignIn(LoginView):
    template_name = 'signin.html'


def playlists(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists.html', {'playlists': playlists})\



def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    songs = playlist.songs.all()
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

# class CreateSong()
