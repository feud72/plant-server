from django.urls import path

from auth.views import GoogleLogin, KakaoLogin

urlpatterns = [
    path("google/", GoogleLogin.as_view(), name="google_login"),
    path("kakao/", KakaoLogin.as_view(), name="kakao_login"),
]
