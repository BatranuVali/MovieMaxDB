from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    rated = models.CharField(max_length=10)
    released = models.DateField()
    runtime = models.CharField(max_length=30)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writer = models.TextField()
    actors = models.TextField()
    plot = models.TextField()
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    awards = models.TextField()
    poster = models.URLField()
    ratings = models.JSONField()
    metascore = models.IntegerField()
    imdb_rating = models.FloatField()
    imdb_votes = models.CharField(max_length=30)
    imdb_id = models.CharField(max_length=20)
    movie_type = models.CharField(max_length=20)
    dvd_release = models.DateField()
    box_office = models.CharField(max_length=100)
    production = models.CharField(max_length=100)
    website = models.URLField()
    response = models.BooleanField()

    def __str__(self):
        return self.title
