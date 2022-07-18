from django.contrib.auth import get_user_model

from rest_framework import serializers

from taxonomy.models import Genus, Species

from .models import Photo

User = get_user_model()


class GenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = ("id", "name", "name_kor")


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ("id", "name", "name_kor")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class PhotoSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    genus = GenusSerializer()
    species = SpeciesSerializer()
    url = serializers.ImageField(use_url=True)
    thumbnail = serializers.ImageField(use_url=True)

    class Meta:
        model = Photo
        fields = (
            "id",
            "owner",
            "genus",
            "species",
            "uploaded_at",
            "url",
            "thumbnail",
            "part",
            "longitude",
            "latitude",
            "place",
        )


class PhotoTaxonomyRelatedSerializer(serializers.ModelSerializer):
    # part = serializers.CharField(source="get_part_display")

    class Meta:
        model = Photo
        fields = (
            "id",
            "url",
            "thumbnail",
        )
