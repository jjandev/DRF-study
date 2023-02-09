from django.urls import path
from .views import MovieList, MovieDetail, actor_list, actor_detail, review_list

urlpatterns = [
    path('movies', MovieList.as_view()),
    path('movies/<int:pk>', MovieDetail.as_view()),
    path('movies/<int:pk>/reviews', review_list),
    path('actors', actor_list),
    path('actors/<int:pk>', actor_detail),
]