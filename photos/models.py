import uuid
from django.utils import timezone
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Photo(models.Model):
    class Part(models.IntegerChoices):
        UNIDENTIFIED = 0
        FLOWER = 1
        LEAF = 2
        FRUIT = 3
        BARK = 4
        WHOLE = 5
        NOT_A_PLANT = 9

    def create_uuid_filename(self, filename, thumbnail=False):
        suffix = filename.split(".")[-1]
        seed = str(self.uploaded_at.timestamp())
        name = uuid.uuid3(uuid.NAMESPACE_DNS, seed)
        if thumbnail:
            name = f"{name}_thumbnail"
        return f"{name}.{suffix}"

    def upload_to(self, filename):
        base_path = "images"
        year_month = timezone.now().strftime("%Y%m")
        filename = self.create_uuid_filename(filename)
        path = "/".join([base_path, year_month, filename])
        return path

    def upload_to_thumbnails(self, filename):
        filename = self.create_uuid_filename(filename, thumbnail=True)
        return f"thumbnails/{filename}"

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="photos",
    )
    family = models.ForeignKey(
        "taxonomy.Family",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="photos",
    )
    genus = models.ForeignKey(
        "taxonomy.Genus",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="photos",
    )
    species = models.ForeignKey(
        "taxonomy.Species",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="photos",
    )
    url = models.ImageField(upload_to=upload_to, max_length=255, blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to=upload_to_thumbnails, max_length=255, blank=True, null=True
    )
    part = models.IntegerField(choices=Part.choices, default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    place = models.CharField(max_length=10, null=True, blank=True)
    is_peer_reviewed = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self) -> str:
        if self.species:
            if self.species.name_kor:
                return self.species.name_kor
            elif self.species.name:
                return self.species.name
        return f"미분류 #{str(self.id)}"

    def delete(self, *args, **kwargs):
        super().save(*args, **kwargs)
