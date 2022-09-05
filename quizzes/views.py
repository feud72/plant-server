from rest_framework.viewsets import ModelViewSet


from .models import Quiz
from .serializers import QuizSerializer
from .services import create_new_quiz


class QuizViewSet(ModelViewSet):
    queryset = (
        Quiz.objects.all()
        .prefetch_related("photos")
        .prefetch_related("photos__species")
    )
    serializer_class = QuizSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        user_id = self.request.user.pk
        if user_id == None:
            return self.queryset[:10]
        else:
            queryset = self.queryset.exclude(answers__user_id=user_id).prefetch_related(
                "answers"
            )
            count = queryset.count()
            if count < 20:
                create_new_quiz()
            return queryset.order_by("?")[:10]
