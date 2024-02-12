from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import MusicForm
from .models import Music
from .serializers import MusicSerializer
from django.contrib import messages


class MusicAddView(View):
    @staticmethod
    def get(request):
        return (form := MusicForm()) and render(request, 'Music/add.html', {'form': form})

    @staticmethod
    def post(request):
        form = MusicForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Music.objects.create(title=cd['title'], artist=cd['artist'], album=cd['album'], year=cd['year'],
                                 genre=cd['genre'], image=cd['image'], audio=cd['audio'])
            messages.success(request, 'Music added successfully', extra_tags='success')
            return redirect('info')
        return render(request, 'Music/add.html', {'form': form})


class MusicInfoView(View):
    @staticmethod
    def get(request):
        music_data = Music.objects.all()
        serializer = MusicSerializer(music_data, many=True)
        return render(request, 'Music/info.html', {'music_data': serializer.data})


class MusicDeleteView(View):
    @staticmethod
    def get(request, music_id):
        (music := get_object_or_404(Music, pk=music_id)) and music.delete()
        messages.success(request, 'Music deleted successfully', extra_tags='success')
        return redirect('info')
