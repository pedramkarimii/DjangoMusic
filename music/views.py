from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicForm
from .models import Music
from .serializers import MusicSerializer
from django.contrib import messages


def add(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Music.objects.create(title=cd['title'], artist=cd['artist'], album=cd['album'], year=cd['year'],
                                 genre=cd['genre'], image=cd['image'], audio=cd['audio'])
            messages.success(request, 'Music added successfully', extra_tags='success')
            return redirect('info')

    else:
        form = MusicForm()
    return render(request, 'Music/add.html', {'form': form})


def info(request):
    music_data = Music.objects.all()
    serializer = MusicSerializer(music_data, many=True)
    return render(request, 'home/home.html', {'music_data': serializer.data})


def delete(request, music_id):
    (music := get_object_or_404(Music, pk=music_id)) and music.delete()
    return render(request, 'Music/delete.html', {'music': music}) and redirect('info')
