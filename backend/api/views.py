from django.contrib.auth.models import User
from datetime import datetime

import requests
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer, UserSerializer


class CreateMovieView(APIView):

    def get(self, request, movie_name):
        try:
            url = f"https://www.omdbapi.com/?t={movie_name}&apikey=43a3b6a0"
            response = requests.get(url)
            data = response.json()

            if 'Error' in data:
                return Response({"message": "Movie not found"})

            released = datetime.strptime(data['Released'], '%d %b %Y').strftime('%Y-%m-%d')
            dvd_release = datetime.strptime(data['DVD'], '%d %b %Y').strftime('%Y-%m-%d')

            title = data['Title']
            if not Movie.objects.filter(title=title).exists():
                movie = Movie(
                    title=data['Title'],
                    year=int(data['Year']) if data['Year'].isdigit() else None,
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
                    metascore=int(data['Metascore']) if data['Metascore'].isdigit() else None,
                    imdb_rating=float(data['imdbRating']) if data['imdbRating'].replace('.', '', 1).isdigit() else None,
                    imdb_votes=data['imdbVotes'],
                    imdb_id=data['imdbID'],
                    movie_type=data['Type'],
                    dvd_release=dvd_release,
                    box_office=data['BoxOffice'],
                    production=data['Production'],
                    website=data['Website'],
                    response=data['Response'] == 'True'
                )
                movie.save()
            else:
                print(f"Movie with title {title} already exists in the database.")

        except requests.exceptions.RequestException as e:
            return Response({"message": f"An error occurred while fetching movie data: {str(e)}"})

        except Exception as e:
            return Response({"message": f"An unexpected error occurred: {str(e)}"})

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
