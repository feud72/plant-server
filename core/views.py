from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.serializers import UserCustomSerializer


User = get_user_model()


# class UserViewSet(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
class UserView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
