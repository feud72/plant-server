from django.contrib.auth import get_user_model

from rest_framework import serializers

UserModel = get_user_model()


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "nickname",
            "date_joined",
            "total_point",
        )
        read_only_fields = (
            "id",
            "username",
            "total_point",
            "date_joined",
        )
