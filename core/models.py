import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    total_point = models.IntegerField(default=0)
    nickname = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.username)
