from django_filters import rest_framework as filters
from photos.models import Photo

from taxonomy.models import Family, Genus, Species


class FamilyFilter(filters.FilterSet):
    query = filters.CharFilter(
        field_name="genera__species__name_kor", label="species", lookup_expr="icontains"
    )

    class Meta:
        fields = ["id", "query"]
        model = Family


class GenusFilter(filters.FilterSet):
    family = filters.NumberFilter(field_name="family", lookup_expr="exact")
    query = filters.CharFilter(field_name="species__name_kor", lookup_expr="icontains")

    class Meta:
        fields = ["family", "query"]
        model = Genus


class SpeciesFilter(filters.FilterSet):
    genus = filters.NumberFilter(field_name="genus", lookup_expr="exact")
    query = filters.CharFilter(field_name="name_kor", lookup_expr="icontains")

    class Meta:
        model = Species
        fields = ["genus", "query"]


class PhotoFilter(filters.FilterSet):
    species = filters.CharFilter(
        field_name="species__name_kor", lookup_expr="icontains"
    )

    class Meta:
        model = Photo
        fields = ["species"]
