from django.contrib.auth import get_user_model

from rest_framework import serializers

from taxonomy.models import Genus, Species

from .models import Photo

from taxonomy.models import Family

User = get_user_model()


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ("id", "name", "name_kor")


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
    family = FamilySerializer()
    genus = GenusSerializer()
    species = SpeciesSerializer()
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


class PhotoTaxonomyRelatedSerializer(serializers.ModelSerializer):
    # part = serializers.CharField(source="get_part_display")

    class Meta:
        model = Photo
        fields = (
            "id",
            "url",
            "thumbnail",
        )


class FilteredThumbnailSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        # data = data.all().first()
        return super(FilteredThumbnailSerializer, self).to_representation(data)


class PhotoThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            "id",
            "thumbnail",
        )
        list_serializer_class = FilteredThumbnailSerializer
