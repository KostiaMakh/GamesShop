from django.urls import path, include
from rest_framework import routers
from shop.api.views import (
    GenreApiView,
    LanguageApiView,
    DeviceApiView,
    CompanyApiView,
    GameApiView,
)

router = routers.DefaultRouter()
router.register('genres', GenreApiView)
router.register('languages', LanguageApiView)
router.register('devices', DeviceApiView)
router.register('companies', CompanyApiView)
router.register('games', GameApiView)


urlpatterns = [
    path('', include(router.urls)),
]
