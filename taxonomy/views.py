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
        Family.objects.prefetch_related("genera").prefetch_related("photos").distinct()
    )
    serializer_class = FamilySerializer
    http_method_names = ["get"]
    pagination_class = None
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FamilyFilter

    def get_serializer_context(self):
        context = {
            "request": self.request,
            "format": self.format_kwarg,
            "view": self,
        }
        query = self.request.query_params.get("query")
        if query != None:
            context.update({"query": query})
        return context


class GenusViewSet(ModelViewSet):
    queryset = (
        Genus.objects.prefetch_related("species")
        .prefetch_related("photos")
        .distinct()
        .order_by(F("name_kor").asc(nulls_last=True))
    )
    serializer_class = GenusSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GenusFilter

    def get_serializer_context(self):
        context = {
            "request": self.request,
            "format": self.format_kwarg,
            "view": self,
        }
        query = self.request.query_params.get("query")
        if query != None:
            context.update({"query": query})
        return context


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
