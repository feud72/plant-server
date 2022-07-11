from rest_framework import serializers

from .models import Family, Genus, Species


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ("id", "name", "name_kor", "pid", "genus")


class GenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = ("id", "family", "name", "name_kor")


class FamilySerializer(serializers.ModelSerializer):
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


class FamilyDetailSerializer(FamilySerializer):
    genera = GenusSmallSerializer(source="genus_set", many=True, read_only=True)

    class Meta(FamilySerializer.Meta):
        fields = ("id", "name", "name_kor", "genera")


class SpeciesDetailSerializer(SpeciesSerializer):
    genus = GenusSerializer(read_only=True)
    family = FamilySerializer(source="genus.family", read_only=True)

    class Meta(SpeciesSerializer.Meta):
        fields = ("id", "name", "name_kor", "family", "genus")


class GenusDetailSerializer(GenusSerializer):
    species = SpeciesSmallSerializer(source="species_set", many=True, read_only=True)
    family = FamilySerializer(read_only=True)

    class Meta(GenusSerializer.Meta):
        fields = ("id", "name", "name_kor", "family", "species")
