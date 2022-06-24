from rest_framework import serializers

from .models import Family, Genus, Species


class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Species
        fields = ("id", "scientific_name", "name_kor", "genus", "url")


class GenusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genus
        fields = ("id", "family", "name", "name_kor", "url")


class FamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Family
        fields = ("id", "name", "name_kor", "url")


class GenusSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = ("id", "name", "name_kor", "url")


class SpeciesSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ("id", "scientific_name", "name_kor", "url")


class FamilyDetailSerializer(serializers.HyperlinkedModelSerializer):
    genera = GenusSmallSerializer(source="genus_set", many=True, read_only=True)

    class Meta:
        model = Family
        fields = ("id", "name", "name_kor", "genera")


class SpeciesDetailSerializer(serializers.HyperlinkedModelSerializer):
    genus = GenusSerializer(read_only=True)
    family = FamilySerializer(source="genus.family", read_only=True)

    class Meta:
        model = Species
        fields = ("id", "scientific_name", "name_kor", "family", "genus")


class GenusDetailSerializer(serializers.HyperlinkedModelSerializer):
    species = SpeciesSmallSerializer(source="species_set", many=True, read_only=True)
    family = FamilySerializer(read_only=True)

    class Meta:
        model = Genus
        fields = ("id", "name", "name_kor", "family", "species")
