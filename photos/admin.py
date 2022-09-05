from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "thumbnail",
        "uploaded_at",
    )
    readonly_fields = ("uploaded_at",)
    search_fields = ["species__name_kor"]
