from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import routers
from .views import (
    MainPage,
    GenrePage,
    GenresList,
    GamesPage,
    FilterGames,
    GameDetail,
    CreateGame,
    CompanyPage,

)
from shop.api.views import (
    GenreApiView,
    LanguageApiView,
    DeviceApiView,
    CompanyApiView,
)

router = routers.DefaultRouter()
router.register('genres', GenreApiView)
router.register('languages', LanguageApiView)
router.register('devices', DeviceApiView)
router.register('companies', CompanyApiView)

urlpatterns = [
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('', MainPage.as_view(), name='home'),
    path('genre/', GenresList.as_view()),
    path('filter/', FilterGames.as_view(), name='filter'),
    path('games/', GamesPage.as_view(), name='games'),
    path('games/<str:slug>/', GameDetail.as_view(), name='game'),
    path('genre/<str:slug>/', GenrePage.as_view(), name='genre'),
    path('company/<str:slug>/', CompanyPage.as_view(), name='company'),
    path('create-game/', CreateGame.as_view(), name='add_game'),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
