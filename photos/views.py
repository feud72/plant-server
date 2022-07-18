from rest_framework.viewsets import ModelViewSet

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
