from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from django.conf import settings

CALLBACK_URL = "https://feud72.pe.kr/accounts/google/callback"

if settings.DEBUG:
    CALLBACK_URL = "http://localhost:8000/accounts/google/callback"


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = CALLBACK_URL
    client_class = OAuth2Client
