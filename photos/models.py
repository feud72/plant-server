from django.db import models

from django.conf import settings


class Photo(models.Model):
    class Part(models.IntegerChoices):
        UNIDENTIFIED = 0
        FLOWER = 1
        LEAF = 2
        FRUIT = 3
        BARK = 4
        WHOLE = 5
        NOT_A_PLANT = 9

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    plant = models.ForeignKey(
        "taxonomy.Species", on_delete=models.CASCADE, blank=True, null=True
    )
    url = models.URLField()
    thumbnail = models.URLField()
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

    def __str__(self) -> str:
        return self.plant.name_kor
