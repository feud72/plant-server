# Generated by Django 4.1b1 on 2022-07-06 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxonomy", "0003_species_pid"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="family",
            options={
                "ordering": ["name_kor"],
                "verbose_name": "Family",
                "verbose_name_plural": "과",
            },
        ),
        migrations.RenameField(
            model_name="species",
            old_name="scientific_name",
            new_name="name",
        ),
    ]