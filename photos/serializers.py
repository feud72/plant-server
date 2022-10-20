from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Photo

from taxonomy.serializers import (
    FamilySimpleSerializer,
    GenusSimpleSerializer,
    SpeciesSimpleSerializer,
)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "nickname", "username")


class PhotoSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    family = FamilySimpleSerializer()
    genus = GenusSimpleSerializer()
    species = SpeciesSimpleSerializer()
    url = serializers.ImageField(use_url=True)
    thumbnail = serializers.ImageField(use_url=True)

    class Meta:
        model = Photo
        fields = (
            "id",
            "owner",
            "family",
            "genus",
            "species",
            "uploaded_at",
            "url",
            "thumbnail",
            "part",
            "upvote",
            "downvote",
            "longitude",
            "latitude",
            "place",
        )


class PhotoQuizeRelatedSerializer(serializers.ModelSerializer):
    species = SpeciesSimpleSerializer()

    class Meta:
        model = Photo
        fields = (
            "species",
            "url",
            "thumbnail",
        )


class FilteredThumbnailSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        return super(FilteredThumbnailSerializer, self).to_representation(data)


class PhotoThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            "id",
            "thumbnail",
        )
        list_serializer_class = FilteredThumbnailSerializer
