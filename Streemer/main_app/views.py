from django import views
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Playlist, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')


class SignIn(LoginView):
    template_name = 'signin.html'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('playlists')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'signup.html', {
        'form': form,
        'error_message': error_message
    })


@login_required
def playlists(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'playlists.html', {'playlists': playlists})\



@login_required
def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    songs = playlist.songs.all()
    return render(request, 'playlist_detail.html', {
        'playlist': playlist,
        'songs': songs,
    })


@login_required
def library(request):
    songs = Song.objects.filter(user=request.user)
    return render(request, 'library.html', {'songs': songs})


@login_required
def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'song_detail.html', {'song': song})


class CreateSong(LoginRequiredMixin, CreateView):
    model = Song
    fields = ['title', 'artist']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateSong(LoginRequiredMixin, UpdateView):
    model = Song
    fields = ['title', 'artist']


class DeleteSong(LoginRequiredMixin, DeleteView):
    model = Song
    success_url = '/library/'


class CreatePlaylist(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ['title']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class UpdatePlaylist(LoginRequiredMixin, UpdateView):
    model = Playlist
    fields = ['songs']

class UpdatePlaylistTitle(LoginRequiredMixin, UpdateView):
    model = Playlist
    fields = ['title']


@login_required
def remove_song(request, playlist_id, song_id):
    playlist = Playlist.objects.get(id=playlist_id)
    playlist.songs.remove(song_id)
    return redirect('playlist-detail', playlist_id=playlist.id)
    

class DeletePlaylist(LoginRequiredMixin, DeleteView):
    model = Playlist
    success_url = '/playlists/'