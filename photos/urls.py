from django.urls import include, path
from rest_framework_nested import routers

from .views import PhotoViewSet

router = routers.DefaultRouter()
router.register("", PhotoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
