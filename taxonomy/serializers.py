from rest_framework import serializers

from .models import Family, Genus, Species

from photos.serializers import (
    PhotoSerializer,
    PhotoThumbnailSerializer,
)


class FilteredGenusSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        if "query" in self.context.keys():
            data = data.filter(species__name_kor__icontains=self.context["query"])
        return super(FilteredGenusSerializer, self).to_representation(data)


class FilteredSpeciesSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        if "query" in self.context.keys():
            data = data.filter(name_kor__icontains=self.context["query"])
        return super(FilteredSpeciesSerializer, self).to_representation(data)


class FamilySmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ("id", "name", "name_kor")


class GenusSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = ("id", "name", "name_kor")
        list_serializer_class = FilteredGenusSerializer


class SpeciesSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ("id", "name", "name_kor")
        list_serializer_class = FilteredSpeciesSerializer


class GenusSerializer(serializers.ModelSerializer):
    children = SpeciesSmallSerializer(source="species", read_only=True, many=True)
    photos = PhotoThumbnailSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Genus
        fields = ("id", "name", "name_kor", "photos", "children")


class FamilySerializer(serializers.ModelSerializer):
    children = GenusSmallSerializer(source="genera", many=True, read_only=True)
    photos = PhotoThumbnailSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Family
        fields = ("id", "name", "name_kor", "photos", "children")


class SpeciesSerializer(serializers.ModelSerializer):
    genus = GenusSmallSerializer(read_only=True)
    family = FamilySmallSerializer(source="genus.family", read_only=True)
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Species
        fields = ("id", "name", "name_kor", "genus", "family", "photos")


class FamilyDetailSerializer(FamilySerializer):
    genera = GenusSmallSerializer(source="genera", many=True, read_only=True)

    class Meta(FamilySerializer.Meta):
        fields = ("id", "name", "name_kor", "genera")


class GenusDetailSerializer(GenusSerializer):
    species = SpeciesSerializer(source="species", many=True, read_only=True)
    family = FamilySerializer(read_only=True)

    class Meta(GenusSerializer.Meta):
        fields = ("id", "name", "name_kor", "family", "species")
