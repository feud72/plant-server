# import random

from rest_framework import serializers

from .models import Quiz

from photos.serializers import PhotoQuizeRelatedSerializer


class QuizSerializer(serializers.ModelSerializer):
    photos = PhotoQuizeRelatedSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["id", "photos"]
