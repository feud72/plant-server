import re
from django.db.models import Count

from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters

from core.filters import PhotoFilter

from .models import Photo
from .serializers import PhotoSerializer


class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    http_method_names = ["get"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PhotoFilter

    def get_queryset(self):
        queryset = (
            Photo.objects.all()
            .prefetch_related("genus")
            .prefetch_related("family")
            .prefetch_related("species")
            .prefetch_related("owner")
        )
        query = self.request.query_params.get("query", None)
        if query != None and query != "":
            reg = re.compile(r"[a-zA-Z]")
            if reg.match(query):
                queryset = queryset.filter(species__name__icontains=query)
            else:
                queryset = queryset.filter(species__name_kor__icontains=query)
        return queryset
