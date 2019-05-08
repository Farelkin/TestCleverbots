from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Snippet
from .serializers import SnippetSerializer, UploadPhotoSerializer
from rest_framework import viewsets


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('date', 'size')
    search_fields = ('date', 'size')
    http_method_names = ['get', 'put', 'patch', 'head', 'delete', 'options']


class UploadPhotoView(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = UploadPhotoSerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        serializer.save(size=serializer.validated_data['image'].size)
