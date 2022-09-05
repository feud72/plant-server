# Generated by Django 4.1 on 2022-08-22 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0003_alter_quiz_photos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="quizzes.quiz",
            ),
        ),
    ]
