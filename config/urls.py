from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from auth.views import GoogleLogin


urlpatterns = [
    path("admin/", admin.site.urls),
    path(settings.ENV.ENV("API_ENDPOINT"), include("core.urls")),
    path("accounts/google/", GoogleLogin.as_view(), name="google_login"),
    path("accounts/", include("dj_rest_auth.urls")),
    path("accounts/", include("allauth.urls")),
    # path("accounts/", include("accounts.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("__debug__", include(debug_toolbar.urls))),
