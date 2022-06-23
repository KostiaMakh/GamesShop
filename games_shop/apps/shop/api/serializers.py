from rest_framework import serializers
from shop.models import (
    Genre,
    Language,
    Device,
    Company,
    Game,
    ScreenShot,
)


class GamePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenShot
        fields = ('screenshot', )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = serializers.ALL_FIELDS


class LanguageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        exclude = (
            'slug',
            'id',
        )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = serializers.ALL_FIELDS


class DeviceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        exclude = (
            'slug',
            'id',
        )


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = serializers.ALL_FIELDS


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = (
            'slug',
            'id',
        )


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = serializers.ALL_FIELDS


class GameSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=False)
    genres = GenreSerializer(many=False)
    languages = LanguageSerializer(many=True)
    devices = DeviceSerializer(many=True)
    screenshots = GamePhotoSerializer(many=True)

    class Meta:
        model = Game
        fields = serializers.ALL_FIELDS
