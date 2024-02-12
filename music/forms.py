from django import forms
from .models import Music


class MusicForm(forms.Form):
    class Meta:
        model = Music
        fields = ['title', 'artist', 'album', 'genres', 'release_date', 'category']
