from django.urls import include, path
from rest_framework_nested import routers

from .views import QuizViewSet

router = routers.DefaultRouter()
router.register("", QuizViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
