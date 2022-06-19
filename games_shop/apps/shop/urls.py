from django.urls import path, include
from .views import (
    MainPage,
    GenrePage,
    GenresList,
    GamesPage,
    FilterGames,
    GameDetail,
    CreateGame,
    CompanyPage
)

urlpatterns = [
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('', MainPage.as_view(), name='home'),
    path('genre/', GenresList.as_view()),
    path('filter/', FilterGames.as_view(), name='filter'),
    path('games/', GamesPage.as_view(), name='games'),
    path('games/<str:slug>/', GameDetail.as_view(), name='game'),
    path('genre/<str:slug>/', GenrePage.as_view(), name='genre'),
    path('company/<str:slug>/', CompanyPage.as_view(), name='company'),
    path('create-game/', CreateGame.as_view(), name='add_game')
]
