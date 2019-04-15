from rest_framework import serializers
from mainapp.models import Snippet
from datetime import datetime

class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'place')

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     place = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     image = serializers.ImageField(max_length=64, allow_empty_file=False, use_url='photos')
#     date = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def date(self):
#         date = {'date': datetime.now()}
#         return date
