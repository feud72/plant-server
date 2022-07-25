from django.urls import include, path
from rest_framework_nested import routers

from .views import (
    FamilyViewSet,
    GenusViewSet,
    FamilyRelatedGenusViewSet,
    RelatedSpeciesViewSet,
    SpeciesViewSet,
)

router = routers.DefaultRouter()
router.register("families", FamilyViewSet)
router.register("genera", GenusViewSet)
router.register("species", SpeciesViewSet)

families_router = routers.NestedSimpleRouter(router, "families", lookup="family")
families_router.register("genera", FamilyRelatedGenusViewSet, basename="family-genera")

genera_router = routers.NestedSimpleRouter(router, "genera", lookup="genera")
genera_router.register("species", RelatedSpeciesViewSet, basename="genera-species")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(families_router.urls)),
    path("", include(genera_router.urls)),
]
