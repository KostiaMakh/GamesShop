from rest_framework import viewsets
from shop.models import (
    Game,
    Genre,
    Promo,
    Company,
    Device,
    Language,
    ScreenShot,
)
from shop.api.serializers import (
    GenreSerializer,
    LanguageSerializer,
    LanguageCreateSerializer,
    DeviceSerializer,
    DeviceCreateSerializer,
    CompanySerializer,
    CompanyCreateSerializer,
)


class GenreApiView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GenreSerializer


class LanguageApiView(viewsets.ModelViewSet):
    queryset = Language.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.request.method == "GET":
            return LanguageSerializer
        else:
            return LanguageCreateSerializer


class DeviceApiView(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DeviceSerializer
        else:
            return DeviceCreateSerializer


class CompanyApiView(viewsets.ModelViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CompanySerializer
        else:
            return CompanyCreateSerializer
