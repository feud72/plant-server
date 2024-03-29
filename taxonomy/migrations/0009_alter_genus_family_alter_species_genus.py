# Generated by Django 4.1 on 2022-08-09 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("taxonomy", "0008_alter_genus_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genus",
            name="family",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="genera",
                to="taxonomy.family",
                verbose_name="과",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="genus",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="species",
                to="taxonomy.genus",
                verbose_name="속",
            ),
        ),
    ]
