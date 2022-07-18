from rest_framework import serializers

from .models import Family, Genus, Species

from photos.serializers import PhotoTaxonomyRelatedSerializer


class FamilySmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ("id", "name", "name_kor")


class GenusSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = ("id", "name", "name_kor")


class SpeciesSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ("id", "name", "name_kor")


class GenusSerializer(serializers.ModelSerializer):
    children = SpeciesSmallSerializer(source="species_set", read_only=True, many=True)
    photos = PhotoTaxonomyRelatedSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Genus
        fields = ("id", "name", "name_kor", "photos", "children")


class FamilySerializer(serializers.ModelSerializer):
    children = GenusSmallSerializer(source="genus_set", many=True, read_only=True)
    # image = serializers.URLField(read_only=True)
    photos = PhotoTaxonomyRelatedSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Family
        fields = ("id", "name", "name_kor", "photos", "children")


class SpeciesSerializer(serializers.ModelSerializer):
    genus = GenusSmallSerializer(read_only=True)
    family = FamilySmallSerializer(source="genus.family", read_only=True)
    photos = PhotoTaxonomyRelatedSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Species
        fields = ("id", "name", "name_kor", "genus", "family", "photos")


class FamilyDetailSerializer(FamilySerializer):
    genera = GenusSmallSerializer(source="genus_set", many=True, read_only=True)

    class Meta(FamilySerializer.Meta):
        fields = ("id", "name", "name_kor", "genera")


class GenusDetailSerializer(GenusSerializer):
    species = SpeciesSerializer(source="species_set", many=True, read_only=True)
    family = FamilySerializer(read_only=True)

    class Meta(GenusSerializer.Meta):
        fields = ("id", "name", "name_kor", "family", "species")
