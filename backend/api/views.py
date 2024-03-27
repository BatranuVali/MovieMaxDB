from django.contrib.auth.models import User
import requests  # Change this line
from datetime import datetime
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer, UserSerializer


class CreateMovieView(APIView):

    def get(self, request, movie_name):
        url = f"https://www.omdbapi.com/?t={movie_name}&apikey=43a3b6a0"
        response = requests.get(url)
        data = response.json()

        released = datetime.strptime(data['Released'], '%d %b %Y').strftime('%Y-%m-%d')
        dvd_release = datetime.strptime(data['DVD'], '%d %b %Y').strftime('%Y-%m-%d')  # Add this line

        movie = Movie(
            title=data['Title'],
            year=int(data['Year']),
            rated=data['Rated'],
            released=released,
            runtime=data['Runtime'],
            genre=data['Genre'],
            director=data['Director'],
            writer=data['Writer'],
            actors=data['Actors'],
            plot=data['Plot'],
            language=data['Language'],
            country=data['Country'],
            awards=data['Awards'],
            poster=data['Poster'],
            ratings=data['Ratings'],
            metascore=int(data['Metascore']),
            imdb_rating=float(data['imdbRating']),
            imdb_votes=data['imdbVotes'],
            imdb_id=data['imdbID'],
            movie_type=data['Type'],
            dvd_release=dvd_release,  # Use the correctly formatted date
            box_office=data['BoxOffice'],
            production=data['Production'],
            website=data['Website'],
            response=data['Response'] == 'True'
        )
        movie.save()

        return Response({"message": "Movie data fetched and stored successfully"})


class ListMoviesView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RetrieveMovieView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
