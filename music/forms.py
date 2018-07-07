from django import forms
from .models import Album,Song


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'title', 'genre', 'logo']
    

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['file_type','song_title','audio_file']