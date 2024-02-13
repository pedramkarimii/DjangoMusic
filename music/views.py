from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.views.generic.edit import View
from .forms import MusicForm
from .models import Music
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Count


class MusicAddView(View):
    model = Music
    form_class = MusicForm()
    template_name = 'Music/add.html'
    success_url = reverse_lazy('info')

    def post(self, request, *args, **kwargs):
        form = MusicForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            self.model.objects.create(
                title=cd['title'],
                artist=cd['artist'],
                album=cd['album'],
                release_date=cd['release_date'],
                # genres=cd['genres'],
                category=cd['category']
                # created_at=cd['created_at'],
                # modified_at=cd['modified_at']
            )
            print(form, "moooooooooodeeeeeeeeeeeeellllllll")

            messages.success(request, 'Music added successfully', extra_tags='success')
            return redirect('info')
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):

        return (form := MusicForm()) and render(request, self.template_name, {'form': form})
    # def dispatch(self, request, *args, **kwargs):
    #     if Music.objects.count() > 0:
    #         messages.warning(request, 'Music already exists', extra_tags='warning')
    #         return redirect('info')
    #     return super().dispatch(request, *args, **kwargs)


class MusicDeleteView(View):
    model = Music
    success_url = reverse_lazy('info')

    def get(self, request, pk):
        if isinstance(pk, int):
            (music := get_object_or_404(self.model, pk=pk)) and music.delete()
        else:
            (music := get_object_or_404(self.model, title=pk)) and music.delete()
        messages.success(request, 'Music deleted successfully', extra_tags='success')
        return redirect('info')


class MusicInfoView(View):
    template_name = 'Music/info.html'

    def get(self, request):
        return (form := Music.objects.all()) and render(request, self.template_name, {'form': form})


class CountAllView(ListView):
    model = Music
    template_name = 'Music/count.html'
    context_object_name = 'music_data'
    queryset = Music.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate counts for each field
        context['title_counts'] = Music.objects.values('title').annotate(count=Count('title'))
        context['artist_counts'] = Music.objects.values('artist').annotate(count=Count('artist'))
        context['album_counts'] = Music.objects.values('album').annotate(count=Count('album'))
        context['category_counts'] = Music.objects.values('category').annotate(count=Count('category'))

        return context
