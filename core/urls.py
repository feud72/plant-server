from django.urls import include, path
from rest_framework import routers

from photos.views import PhotoViewSet
from taxonomy.views import (
    FamilyViewSet,
    GenusViewSet,
    SpeciesViewSet,
)
from quizzes.views import QuizViewSet

router = routers.DefaultRouter()
router.register("photos", PhotoViewSet)
router.register("families", FamilyViewSet, basename="family")
router.register("genera", GenusViewSet)
router.register("species", SpeciesViewSet)
router.register("quizzes", QuizViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("accounts/", include("auth.urls")),
    path("accounts/", include("dj_rest_auth.urls")),
    path("accounts/", include("allauth.urls")),
]
