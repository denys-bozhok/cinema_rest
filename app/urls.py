from django.urls import path
from .views import Movies, Tickets, user, users, Places


urlpatterns = [
    path('movies', Movies.as_view({
        'get': 'movies',
        'post': 'create_movie'
        })),
    
    path('movie/<int:arg>', Movies.as_view({
        'get': 'movie',
        'delete': 'delete_movie',
        'put': 'put_movie'
        })),
    
    path('ticket/<int:arg>', Tickets.as_view()),
    
    path('user/<int:arg>', user),
    
    path('users', users),
    
    path('places', Places.places),
    
    path('place/<int:arg>', Places.place),
]