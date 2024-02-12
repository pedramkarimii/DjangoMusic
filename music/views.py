# from django.http import Http404
# from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView, DeleteView
from django.views.generic.edit import View
# from django.views import View
from .forms import MusicForm
from .models import Music, Artist, Genre, Album
# from .serializers import MusicSerializer
from django.contrib import messages
from django.urls import reverse_lazy


# from django.http import Http404


#
# class MusicAddView(View):
#     @staticmethod
#     def get(request):
#         return (form := MusicForm()) and render(request, 'Music/add.html', {'form': form})
#
#     @staticmethod
#     def post(request):
#         form = MusicForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             Music.objects.create(title=cd['title'], artist=cd['artist'], album=cd['album'], year=cd['year'],
#                                  genre=cd['genre'], image=cd['image'], audio=cd['audio'])
#             messages.success(request, 'Music added successfully', extra_tags='success')
#             return redirect('info')
#         return render(request, 'Music/add.html', {'form': form})
# class MusicAddView(CreateView):
#     model = Music
#     form_class = MusicForm
#     template_name = 'Music/add.html'
#     success_url = reverse_lazy('info')
#
#     def form_valid(self, form):
#         messages.success(self.request, 'Music added successfully', extra_tags='success')
#         return super().form_valid(form), redirect('Main')


class MusicAddView(View):
    model = Music
    form_class = MusicForm
    template_name = 'Music/add.html'
    success_url = reverse_lazy('info')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(form , "formmmmmmmmmmmmmmmmm")
        if form.is_valid():
            cd = form.cleaned_data
            print(cd , "cdddddddddddddddddddddddd")
            if Music.objects.exists():
                messages.error(request, 'Music already exists')
            else:
                # Create the Music object
                Music.objects.create(
                    title=cd.get('title'),
                    artist=cd.get('artist'),
                    album=cd.get('album'),
                    genres=cd.get('genres'),
                    category=cd.get('category'),
                    release_date=cd.get('release_date')
                )

                messages.success(request, 'Music added successfully', extra_tags='success')
                return redirect('info')
        else:
            # If the form is not valid, render it again with errors
            return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    # def dispatch(self, request, *args, **kwargs):
    #     if request.method == 'POST' and Music.objects.exists():
    #         raise Http404("Music object already exists")
    #     return super().dispatch(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})


# class MusicInfoView(View):
#     @staticmethod
#     def get(request):
#         music_data = Music.objects.all()
#         serializer = MusicSerializer(music_data, many=True)
#         return render(request, 'Music/info.html', {'music_data': serializer.data})
class CountAllView(ListView):
    model = Music
    template_name = 'Music/info.html'
    context_object_name = 'music_data'


# class MusicDeleteView(View):
#     @staticmethod
#     def get(request, music_id):
#         (music := get_object_or_404(Music, pk=music_id)) and music.delete()
#         messages.success(request, 'Music deleted successfully', extra_tags='success')
#         return redirect('info')
# class MusicDeleteView(DeleteView):
#     model = Music
#     success_url = reverse_lazy('info')
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.delete()
#         messages.success(request, 'Music deleted successfully', extra_tags='success')
#         return super().delete(request, *args, **kwargs), redirect('Main')

class MusicDeleteView(DeleteView):
    model = Music
    template_name = 'Music/delete.html'
    success_url = reverse_lazy('info')

    # def get_object(self):
    #     # Get object by id or title
    #     queryset = self.get_queryset()
    #     filter_kwargs = {'id': self.kwargs.get('pk')}
    #     if queryset.filter(**filter_kwargs).exists():
    #         return queryset.get(**filter_kwargs)
    #     filter_kwargs = {'title': self.kwargs.get('pk')}
    #     if queryset.filter(**filter_kwargs).exists():
    #         return queryset.get(**filter_kwargs)
    #     return None
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, 'Music deleted successfully', extra_tags='success')
        return super().delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Get the object to be deleted. Raises a 404 error if the object does not exist.
        """
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        return obj


# def count_all(request):
#     artist_count = Artist.objects.count()
#     album_count = Album.objects.count()
#     genre_count = Genre.objects.count()
#     music_count = Music.objects.count()
#
#     context = {
#         'artist_count': artist_count,
#         'album_count': album_count,
#         'genre_count': genre_count,
#         'music_count': music_count,
#     }
#     return render(request, 'Music/count.html', context)


class MusicInfoView(TemplateView):
    template_name = 'Music/count.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist_count'] = Artist.objects.count()
        context['album_count'] = Album.objects.count()
        context['genre_count'] = Genre.objects.count()
        context['music_count'] = Music.objects.count()
        return context
