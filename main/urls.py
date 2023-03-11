from django.urls import path
from main import views

urlpatterns = {
    path("", views.main, name='main'),
    path("profile", views.profile, name='profile'),
    path("playlists", views.playlists, name='playlists'),
    path("playlists-create", views.playlists_create, name='playlists-create'),
    path("add_song", views.add_song, name='add_song'),
    path("remove_song", views.remove_song, name='remove_song'),
    path("create", views.create, name='create'),
    path("search", views.search, name='search'),
    path("playlists-view", views.playlists_view, name='playlists-view'),
    path("play-songs", views.play_songs, name='play-songs'),
    path("sort", views.sort, name='sort'),
    path("playlists-genre", views.playlists_genre, name='playlists-genre'),
    path("playlists-length", views.playlists_length, name='playlists-length'),
    path("random", views.random, name='random'),
}