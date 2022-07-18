from django.db import models
from django.conf import settings
from django.utils.functional import cached_property

from photos.models import Photo


class Family(models.Model):
    name = models.CharField(verbose_name="과", max_length=100, unique=True)
    name_kor = models.CharField(
        verbose_name="과국명", max_length=100, blank=True, null=True
    )

    class Meta:
        verbose_name = "Family"
        verbose_name_plural = "과"
        ordering = ["name_kor"]

    def __str__(self) -> str:
        return self.name_kor

    @property
    def image(self):
        photo = Photo.objects.filter(family=self.id).first().thumbnail

        return f"{settings.MEDIA_URL}{photo}"


class Genus(models.Model):
    family = models.ForeignKey(
        "taxonomy.Family", on_delete=models.CASCADE, verbose_name="과"
    )
    name = models.CharField(verbose_name="속", max_length=100, unique=True)
    name_kor = models.CharField(
        verbose_name="속국명", max_length=100, blank=True, null=True
    )

    class Meta:
        verbose_name = "Genus"
        verbose_name_plural = "속"
        ordering = ["name_kor"]

    def __str__(self) -> str:
        return self.name

    @property
    def image(self):
        photo = Photo.objects.filter(genus=self.id).first().thumbnail
        return f"{settings.MEDIA_URL}{photo}"


class Species(models.Model):
    genus = models.ForeignKey(
        "taxonomy.Genus", on_delete=models.CASCADE, verbose_name="속"
    )
    name = models.CharField(verbose_name="학명", max_length=200, unique=True)
    name_kor = models.CharField(
        verbose_name="국명", max_length=100, blank=True, null=True
    )
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Species"
        verbose_name_plural = "종"

    def __str__(self) -> str:
        return self.name
