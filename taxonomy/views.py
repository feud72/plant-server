from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from .models import Family, Genus, Species
from .serializers import (
    FamilySerializer,
    FamilyDetailSerializer,
    GenusSerializer,
    GenusDetailSerializer,
    SpeciesDetailSerializer,
    SpeciesSerializer,
)

from core.filters import FamilyFilter, GenusFilter, SpeciesFilter


class FamilyViewSet(ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = {
        "list": FamilySerializer,
        "retrieve": FamilyDetailSerializer,
    }
    default_serializer_class = FamilySerializer
    http_method_names = ["get"]
    pagination_class = None
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FamilyFilter

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.default_serializer_class)


class GenusViewSet(ModelViewSet):
    queryset = Genus.objects.all()
    serializer_class = {
        "list": GenusSerializer,
        "retrieve": GenusDetailSerializer,
    }
    default_serializer_class = GenusSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GenusFilter

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.default_serializer_class)


class SpeciesViewSet(ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = {
        "list": SpeciesSerializer,
        "retrieve": SpeciesDetailSerializer,
    }
    default_serializer_class = SpeciesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SpeciesFilter

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.default_serializer_class)
