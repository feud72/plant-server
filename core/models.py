import uuid

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    total_point = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.username)
