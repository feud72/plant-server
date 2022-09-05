from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Quiz(models.Model):
    photos = models.ManyToManyField("photos.Photo", related_name="quizzes", blank=True)
    correct_answer = models.IntegerField(
        validators=[MaxValueValidator(4), MinValueValidator(1)]
    )


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quiz = models.ForeignKey(
        "quizzes.Quiz", on_delete=models.CASCADE, related_name="answers"
    )
    answer = models.IntegerField(
        validators=[MaxValueValidator(4), MinValueValidator(1)]
    )
    is_correct = models.BooleanField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_correct == None:
            self.is_correct = self.answer == self.quiz.correct_answer
        return super().save(*args, **kwargs)
