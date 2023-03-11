from django.db import models

class Playlists(models.Model):
    email = models.CharField(max_length = 50)
    play_list_name = models.CharField(max_length = 50)
    song_name = models.CharField(max_length = 50)
    song_artist = models.DateField()
    song_image = models.CharField(max_length = 200)
    song_audio = models.CharField(max_length = 200)