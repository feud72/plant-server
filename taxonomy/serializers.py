from rest_framework import serializers

from photos.models import Photo

from .models import Family, Genus, Species


class FamilySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ("id", "name", "name_kor")


class GenusSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = ("id", "name", "name_kor")


class SpeciesSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ("id", "name", "name_kor")


class PhotoTaxonomyRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("id", "url", "thumbnail")


class GenusSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        model = Genus
        fields = ("id", "name", "name_kor", "thumbnail", "count")

    def get_thumbnail(self, obj):
        photo = obj.photos.first()
        if photo is None:
            return None
        return photo.thumbnail.url


class FamilySerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        model = Family
        fields = ("id", "name", "name_kor", "thumbnail", "count")

    def get_thumbnail(self, obj: Family):
        photo = obj.photos.first()
        if photo is None:
            return None
        return photo.thumbnail.url


class SpeciesSerializer(serializers.ModelSerializer):
    genus = GenusSimpleSerializer(read_only=True)
    family = FamilySimpleSerializer(source="genus.family", read_only=True)
    photos = PhotoTaxonomyRelatedSerializer(many=True, read_only=True)

    class Meta:
        model = Species
        fields = ("id", "name", "name_kor", "genus", "family", "photos")
