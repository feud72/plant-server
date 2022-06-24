from rest_framework.viewsets import ModelViewSet

from .models import Family, Genus, Species
from .serializers import (
    FamilySerializer,
    FamilyDetailSerializer,
    GenusSerializer,
    GenusDetailSerializer,
    SpeciesDetailSerializer,
    SpeciesSerializer,
)


class FamilyViewSet(ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = {
        "list": FamilySerializer,
        "retrieve": FamilyDetailSerializer,
    }
    default_serializer_class = FamilySerializer

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.default_serializer_class)


class GenusViewSet(ModelViewSet):
    queryset = Genus.objects.all()
    serializer_class = {
        "list": GenusSerializer,
        "retrieve": GenusDetailSerializer,
    }
    default_serializer_class = GenusSerializer

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.default_serializer_class)


class SpeciesViewSet(ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = {
        "list": SpeciesSerializer,
        "retrieve": SpeciesDetailSerializer,
    }
    default_serializer_class = SpeciesSerializer

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.default_serializer_class)
