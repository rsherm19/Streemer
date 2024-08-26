from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('library')



class Playlist(models.Model):
    title = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('playlists')