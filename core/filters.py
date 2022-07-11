from django_filters import rest_framework as filters

from taxonomy.models import Family, Genus, Species


class BaseTaxonomyFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="istartswith")
    name_kor = filters.CharFilter(field_name="name_kor", lookup_expr="istartswith")

    class Meta:
        fields = ["name", "name_kor"]


class FamilyFilter(BaseTaxonomyFilter):
    class Meta(BaseTaxonomyFilter.Meta):
        model = Family


class GenusFilter(BaseTaxonomyFilter):
    class Meta(BaseTaxonomyFilter.Meta):
        model = Genus


class SpeciesFilter(BaseTaxonomyFilter):
    class Meta(BaseTaxonomyFilter.Meta):
        model = Species
