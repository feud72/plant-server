from django.urls import include, path
from rest_framework import routers

from photos.views import PhotoViewSet
from taxonomy.views import (
    FamilyViewSet,
    GenusViewSet,
    SpeciesViewSet,
)

router = routers.DefaultRouter()
router.register("photos", PhotoViewSet)
router.register("families", FamilyViewSet, basename="family")
router.register("genera", GenusViewSet)
router.register("species", SpeciesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
