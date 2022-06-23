from django.urls import path, include
from rest_framework import routers
from user.api.views import UserCreateApiView, CustomObtainAuthToken

router = routers.DefaultRouter()
router.register('users', UserCreateApiView)

urlpatterns = [
    path('api-token-auth/', CustomObtainAuthToken.as_view()),
    path('', include(router.urls)),
]
