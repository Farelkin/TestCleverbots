from rest_framework import serializers
from mainapp.models import Snippet
import os
from cleverbots import settings


class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    size2 = serializers.SerializerMethodField('get_image_size')
    print(type(size2))

    class Meta:
        model = Snippet
        fields = ('id', 'place', 'image', 'date', 'size2', 'size',)

    def get_image_size(self, obj):
        print(type(os.path.getsize(settings.BASE_DIR + obj.image.url)))
        return os.path.getsize(settings.BASE_DIR + obj.image.url)
