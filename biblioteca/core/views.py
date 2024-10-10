from rest_framework import generics
from .models import Livro, Categoria, Autor
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer
from .filters import LivroFilter

# Clara
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-list"
    filterset_class = LivroFilter
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']
    
class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"
 
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    ordering_fields = ['nome']
    search_fields = ['^nome']
    name = "Categoria-list"
    
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "Categoria-detail"
 
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    ordering_fields = ['nome']
    search_fields = ['^nome']
    name = "Autor-list"
 
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "Autor-detail"


