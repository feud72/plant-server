import random

from .models import Quiz

from photos.models import Photo


def create_new_quiz():
    random_indices = [random.randint(1, 4) for _ in range(10)]
    photo_ids = (
        Photo.objects.filter(species__isnull=False)
        .order_by("?")[:40]
        .values_list("id", flat=True)
    )
    quizzes = Quiz.objects.bulk_create(
        [Quiz(correct_answer=correct_answer) for correct_answer in random_indices]
    )

    for n, quiz in enumerate(quizzes):
        photo_to_quiz_list = []
        for i in range(4):
            photo = Quiz.photos.through(quiz_id=quiz.id, photo_id=photo_ids[4 * n + i])
            photo_to_quiz_list.append(photo)
        Quiz.photos.through.objects.bulk_create(photo_to_quiz_list)
