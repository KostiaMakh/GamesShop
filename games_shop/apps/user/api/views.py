from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from user.models import User
from .serializers import (
    UserCreateSerializer,
    UserSerializer
)


class UserCreateApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer
        elif self.request.method == "GET":
            return UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny(), ]
        else:
            return [permission() for permission in self.permission_classes]
