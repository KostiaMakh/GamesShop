from django.urls import path, include
from rest_framework import routers
from .views import user_login, user_register, user_logout
from user.api.views import UserCreateApiView

router1 = routers.DefaultRouter()
router1.register('registration', UserCreateApiView)

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('api/v1/', include(router1.urls)),
]
