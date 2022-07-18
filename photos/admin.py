from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    # list_display = (
    #     "species",
    #     "thumbnail",
    # )
    # readonly_fields = ("uploaded_at",)

    # @admin.display(description="종")
    # def species(self, obj: Photo):
    #     return "%s" % (obj.plant.name_kor)
    pass
