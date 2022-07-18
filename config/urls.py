from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("taxonomy.urls")),
    path("photos/", include("photos.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("__debug__", include(debug_toolbar.urls))),
