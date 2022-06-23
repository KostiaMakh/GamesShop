from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.authtoken.views import ObtainAuthToken
from user.models import User
from .serializers import (
    UserCreateSerializer,
    UserSerializer,
    CustomAuthTokenSerializer
)


class UserCreateApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()

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


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )
