from django.db import models

from django.contrib.auth import User


class Photo(models.Model):
    class Part(models.IntegerChoices):
        UNIDENTIFIED = 0
        FLOWER = 1
        LEAF = 2
        FRUIT = 3
        BARK = 4
        WHOLE = 5
        NOT_A_PLANT = 9

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    plant = models.ForeignKey(
        "taxonomy.Species", on_delete=models.CASCADE, blank=True, null=True
    )
    part = models.IntegerField(choices=Part.choices, max_length=1, default=0)
    url = models.URLField()
    thumbnail = models.URLField()
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
    is_validated = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
