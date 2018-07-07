# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models 

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=200)
    title  = models.CharField(max_length=200)
    genre  = models.CharField(max_length=200)
    logo   = models.FileField()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse("music:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=20)
    song_title = models.CharField(max_length=100)
    audio_file = models.FileField(default='')

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse("music:home")

    def __str__(self):
        return self.song_title