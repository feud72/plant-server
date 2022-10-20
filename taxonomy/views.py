import re

from django.db.models import F, Count

from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters

from .models import Family, Genus, Species
from .serializers import (
    FamilySerializer,
    GenusSerializer,
    SpeciesSerializer,
)
from .paginations import FamilyPagination

from core.filters import GenusFilter, SpeciesFilter


class FamilyViewSet(ModelViewSet):
    serializer_class = FamilySerializer
    http_method_names = ["get"]
    pagination_class = FamilyPagination

    def get_queryset(self):
        queryset = (
            Family.objects.prefetch_related("genera")
            .prefetch_related("genera__species")
            .prefetch_related("photos")
            .order_by(F("name_kor").asc(nulls_last=True))
        )
        query = self.request.query_params.get("query", None)
        if query != None and query != "":
            reg = re.compile(r"[a-zA-Z]")
            if reg.match(query):
                queryset = queryset.filter(genera__species__name__icontains=query)
            else:
                queryset = queryset.filter(genera__species__name_kor__icontains=query)
        return queryset.annotate(count=Count("genera__species", distinct=True))


class GenusViewSet(ModelViewSet):
    serializer_class = GenusSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GenusFilter

    def get_queryset(self):
        queryset = Genus.objects.prefetch_related("photos").order_by(
            F("name_kor").asc(nulls_last=True)
        )
        query = self.request.query_params.get("query")
        if query != None and query != "":
            reg = re.compile(r"[a-zA-Z]")
            if reg.match(query):
                queryset = queryset.filter(species__name__icontains=query)
            else:
                queryset = queryset.filter(species__name_kor__icontains=query)
        return queryset.annotate(count=Count("species", distinct=True))


class SpeciesViewSet(ModelViewSet):
    queryset = (
        Species.objects.all()
        .prefetch_related("genus")
        .prefetch_related("genus__family")
        .prefetch_related("photos")
        .order_by(F("name_kor").asc(nulls_last=True))
        .distinct()
    )
    serializer_class = SpeciesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SpeciesFilter

    def get_queryset(self):
        queryset = self.queryset
        query = self.request.query_params.get("query")
        if query != None and query != "":
            reg = re.compile(r"[a-zA-Z]")
            if reg.match(query):
                queryset = queryset.filter(name__icontains=query)
            else:
                queryset = queryset.filter(name_kor__icontains=query)
        return queryset.annotate(count=Count("id", distinct=True))
