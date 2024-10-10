from django_filters import rest_framework as filters
from .models import Livro

#Clara

class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')
    categoria = filters.AllValuesFilter(field_name='categoria__nome')
    autor_exato = filters.AllValuesFilter(field_name='autor__nome')
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria']