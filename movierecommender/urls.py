

from django.urls import path
from . import views


app_name = 'movierecommender'

urlpatterns = [
    # route is a string contains a URL pattern
    path('', views.movie_recommendation_view, name='recommendations'),
]
