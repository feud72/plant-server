from django.urls import include, path
from rest_framework import routers

from .views import (
    FamilyViewSet,
    GenusViewSet,
    SpeciesViewSet,
)

router = routers.DefaultRouter()
router.register("families", FamilyViewSet, basename="family")
router.register("genera", GenusViewSet, basename="genera")
router.register("species", SpeciesViewSet, basename="species")

urlpatterns = [
    path("", include(router.urls)),
]
