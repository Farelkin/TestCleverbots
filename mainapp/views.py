from mainapp.models import Snippet
from mainapp.serializers import SnippetSerializer
from rest_framework import viewsets


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

