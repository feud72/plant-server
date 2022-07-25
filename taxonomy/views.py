from django.db.models import F
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from .models import Family, Genus, Species
from .serializers import (
    FamilySerializer,
    GenusSerializer,
    SpeciesSerializer,
)

from core.filters import FamilyFilter, GenusFilter, SpeciesFilter


class FamilyViewSet(ModelViewSet):
    queryset = (
        Family.objects.all().prefetch_related("genus_set").prefetch_related("photos")
    )
    serializer_class = FamilySerializer
    http_method_names = ["get"]
    pagination_class = None
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FamilyFilter


class GenusViewSet(ModelViewSet):
    queryset = (
        Genus.objects.all().prefetch_related("species_set").prefetch_related("photos")
    )
    serializer_class = GenusSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GenusFilter


class FamilyRelatedGenusViewSet(ModelViewSet):
    serializer_class = GenusSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GenusFilter
    pagination_class = None

    def get_queryset(self):
        return (
            Genus.objects.filter(family=self.kwargs["family_pk"])
            .prefetch_related("species_set")
            .prefetch_related("photos")
            .order_by(F("name_kor").asc(nulls_last=True))
        )


class RelatedSpeciesViewSet(ModelViewSet):
    serializer_class = SpeciesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    pagination_class = None

    def get_queryset(self):
        return (
            Species.objects.filter(genus=self.kwargs["genera_pk"])
            .prefetch_related("photos")
            .order_by(F("name_kor").asc(nulls_last=True))
        )


class SpeciesViewSet(ModelViewSet):
    queryset = (
        Species.objects.all()
        .select_related("genus")
        .select_related("genus__family")
        .prefetch_related("photos")
    )
    serializer_class = SpeciesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SpeciesFilter
