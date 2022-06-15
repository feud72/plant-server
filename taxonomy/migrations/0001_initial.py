# Generated by Django 4.1a1 on 2022-06-15 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Family",
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
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="과"),
                ),
                (
                    "name_kor",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="과국명"
                    ),
                ),
            ],
            options={
                "verbose_name": "Family",
                "verbose_name_plural": "과",
            },
        ),
        migrations.CreateModel(
            name="Genus",
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
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="속"),
                ),
                (
                    "name_kor",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="속국명"
                    ),
                ),
                (
                    "family",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="taxonomy.family",
                        verbose_name="과",
                    ),
                ),
            ],
            options={
                "verbose_name": "Genus",
                "verbose_name_plural": "속",
            },
        ),
        migrations.CreateModel(
            name="Species",
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
                    "scientific_name",
                    models.CharField(max_length=100, unique=True, verbose_name="학명"),
                ),
                (
                    "name_kor",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="국명"
                    ),
                ),
                (
                    "genus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="taxonomy.genus",
                        verbose_name="속",
                    ),
                ),
            ],
            options={
                "verbose_name": "Species",
                "verbose_name_plural": "종",
            },
        ),
    ]
