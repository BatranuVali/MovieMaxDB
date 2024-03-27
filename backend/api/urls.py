from django.urls import path
from . import views

urlpatterns = [
    path('fetch_movie/<str:movie_name>/', views.CreateMovieView.as_view()),
    path('movies/', views.ListMoviesView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.RetrieveMovieView.as_view()),
]
