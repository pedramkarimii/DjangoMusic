from django import forms
# from .models import Music


class MusicForm(forms.Form):
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=100)
    album = forms.CharField(max_length=100)
    release_date = forms.DateField()
    # genres = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    # created_at = forms.DateTimeField()
    # modified_at = forms.DateTimeField()

    # class Meta:
    #     model = Music
    #     fields = ['title', 'artist', 'album', 'release_date', 'genres', 'category']

    # def save(self):
    #     return Music.objects.create(**self.cleaned_data)

# class MusicForm(forms.ModelForm):
#     class Meta:
#         model = Music
#         fields = ['title', 'artist', 'album', 'release_date', 'genres', 'category', 'created_at', 'modified_at']
