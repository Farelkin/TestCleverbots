from rest_framework import serializers
from mainapp.models import Snippet
import os
from cleverbots import settings


class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Snippet
        fields = ('place', 'image', 'date', 'size')

