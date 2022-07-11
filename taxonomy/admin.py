from django.contrib import admin

from . import models


@admin.register(models.Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ["name_kor", "name"]
    ordering = ["name_kor"]


@admin.register(models.Genus)
class GenusAdmin(admin.ModelAdmin):
    list_display = ["name", "name_kor", "family", "family_eng"]
    search_fields = ["family__name", "family__name_kor", "name_kor", "name"]
    ordering = ["family__name_kor", "name"]

    @admin.display(description="과 영문명")
    def family_eng(self, obj: models.Species):
        return "%s" % (obj.family.name)


@admin.register(models.Species)
class SpeciesAdmin(admin.ModelAdmin):
    readonly_fields = ("family",)
    list_display = [
        "name_kor",
        "family",
        "name",
        "pid",
    ]
    search_fields = ["genus__name", "name_kor", "name"]
    ordering = ["name_kor"]

    @admin.display(description="과")
    def family(self, obj: models.Species):
        return "%s" % (obj.genus.family.name_kor)
