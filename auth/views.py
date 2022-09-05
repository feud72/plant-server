from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from django.conf import settings

GOOGLE_CALLBACK_URL = (
    f"https://{settings.ENV.ENV('PRODUCT_HOST_IP')}/accounts/google/callback"
)
KAKAO_CALLBACK_URL = (
    f"https://{settings.ENV.ENV('PRODUCT_HOST_IP')}/accounts/kakao/callback"
)

if settings.DEBUG:
    GOOGLE_CALLBACK_URL = "http://127.0.0.1:8000/accounts/google/callback"
    KAKAO_CALLBACK_URL = f"http://127.0.0.1:8000/accounts/kakao/callback"


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URL
    client_class = OAuth2Client


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    callback_url = KAKAO_CALLBACK_URL
    client_class = OAuth2Client
