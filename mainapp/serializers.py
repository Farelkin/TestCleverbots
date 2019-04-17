from rest_framework import serializers
from mainapp.models import Snippet
import os
from cleverbots import settings


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    size = serializers.SerializerMethodField('get_image_size')

    class Meta:
        model = Snippet
        fields = ('id', 'place', 'image', 'date', 'size')

    def get_image_size(self, obj):
        return os.path.getsize(settings.BASE_DIR + obj.image.url)
