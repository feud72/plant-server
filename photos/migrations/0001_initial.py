# Generated by Django 4.1b1 on 2022-07-18 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import photos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taxonomy", "0008_alter_genus_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "url",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        null=True,
                        upload_to=photos.models.Photo.upload_to,
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        null=True,
                        upload_to=photos.models.Photo.upload_to_thumbnails,
                    ),
                ),
                (
                    "part",
                    models.IntegerField(
                        choices=[
                            (0, "Unidentified"),
                            (1, "Flower"),
                            (2, "Leaf"),
                            (3, "Fruit"),
                            (4, "Bark"),
                            (5, "Whole"),
                            (9, "Not A Plant"),
                        ],
                        default=0,
                    ),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                ("upvote", models.IntegerField(default=0)),
                ("downvote", models.IntegerField(default=0)),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=9, null=True
                    ),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=9, null=True
                    ),
                ),
                ("place", models.CharField(blank=True, max_length=10, null=True)),
                ("is_peer_reviewed", models.BooleanField(default=False)),
                ("is_published", models.BooleanField(default=False)),
                (
                    "family",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="taxonomy.family",
                    ),
                ),
                (
                    "genus",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="taxonomy.genus",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "species",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="taxonomy.species",
                    ),
                ),
            ],
            options={
                "ordering": ["-uploaded_at"],
            },
        ),
    ]
