from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters

from core.filters import PhotoFilter

from .models import Photo
from .serializers import PhotoSerializer


class PhotoViewSet(ModelViewSet):
    queryset = (
        Photo.objects.all()
        .prefetch_related("genus")
        .prefetch_related("species")
        .prefetch_related("owner")
    )
    serializer_class = PhotoSerializer
    http_method_names = ["get"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PhotoFilter
