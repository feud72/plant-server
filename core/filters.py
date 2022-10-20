from django_filters import rest_framework as filters
from photos.models import Photo

from taxonomy.models import Genus, Species


class GenusFilter(filters.FilterSet):
    family = filters.NumberFilter(field_name="family", lookup_expr="exact")

    class Meta:
        fields = ["family"]
        model = Genus


class SpeciesFilter(filters.FilterSet):
    family = filters.NumberFilter(field_name="genus__family", lookup_expr="exact")
    genus = filters.NumberFilter(field_name="genus", lookup_expr="exact")

    class Meta:
        model = Species
        fields = ["family", "genus"]


class PhotoFilter(filters.FilterSet):
    family = filters.NumberFilter(field_name="family", lookup_expr="exact")
    genus = filters.NumberFilter(field_name="genus", lookup_expr="exact")

    class Meta:
        model = Photo
        fields = ["family", "genus"]
