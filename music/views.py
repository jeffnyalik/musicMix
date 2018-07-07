# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from django.views import generic
from django.views.generic.edit import UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album,Song

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

class HomeView(generic.ListView):
    model = Album
    template_name = 'music/home.html'
    context_object_name = 'tags'

class DetailPageView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
    context_object_name ='detail_tags'

class CreateAlbum(generic.CreateView):
    model = Album
    template_name = 'music/album_form.html'
    # fields = ['artist', 'title', 'genre', 'logo']
    fields = '__all__'

class UpdateAlbum(UpdateView):
    model = Album
    fields = '__all__'

class AlbumDelete(DeleteView):
    model = Album 
    success_url = reverse_lazy('music:home')
    template_name = 'music/album_delete.html'
    context_object_name ='d'

class CreateSong(generic.CreateView):
    model = Song
    fields = '__all__'
    success_url = reverse_lazy('music:home')
    


class SongList(generic.ListView):
    model = Song
    template_name = 'music/songs.html'
    context_object_name = 'all_songs'

class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:home')
    template_name = 'music/song_delete.html'
    context_object_name = 'erase'
