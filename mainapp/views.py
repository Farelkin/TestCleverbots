from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from mainapp.models import Snippet
from mainapp.serializers import SnippetSerializer
from rest_framework import viewsets


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('date', 'size')
    search_fields = ('date', 'size')
