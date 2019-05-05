from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Snippet
        fields = ('place', 'image', 'date', 'size')


class UploadPhotoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Snippet
        fields = ('place', 'image')
