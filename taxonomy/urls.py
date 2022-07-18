from django.urls import include, path
from rest_framework_nested import routers

from .views import (
    FamilyViewSet,
    GenusViewSet,
    FamilyRelatedGenusViewSet,
    SpeciesViewSet,
)

router = routers.DefaultRouter()
router.register("families", FamilyViewSet)
router.register("genera", GenusViewSet)
router.register("species", SpeciesViewSet)

families_router = routers.NestedSimpleRouter(router, "families", lookup="family")
families_router.register("genera", FamilyRelatedGenusViewSet, basename="family-genera")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(families_router.urls)),
]
