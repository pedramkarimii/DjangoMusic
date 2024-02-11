from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums_artist')
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics_artist')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musics_album')
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    rating = models.IntegerField(default=50, validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def overall_rating(self):
        total_votes = self.likes + self.dislikes
        return self.likes / total_votes if total_votes > 0 else 0.5

    @property
    def average_rating(self):
        return self.rating / 100

    def increment_likes(self):
        self.likes += 1
        self.save()

    def increment_dislikes(self):
        self.dislikes += 1
        self.save()

    @classmethod
    def get_top_rated(cls, count=5):
        return cls.objects.order_by('-overall_rating')[:count]

    def __str__(self):
        return self.title
