from django.urls import include, path
from rest_framework import routers

from .views import (
    FamilyViewSet,
    GenusViewSet,
    SpeciesViewSet,
)

router = routers.DefaultRouter()
router.register("families", FamilyViewSet, basename="family")
router.register("genera", GenusViewSet)
router.register("species", SpeciesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
