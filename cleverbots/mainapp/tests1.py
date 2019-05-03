from django.test import TestCase
# from .models import Snippet
#
#
# class SnippetTest(TestCase):
#     def upload(self):
#         Snippet.objects.create(place='test place', image='cleverbots/static/test/favicon.png')
#
#     def run_upload(self):
#         favicon = Snippet.objects.get(place='test place')
#         self.assertEqual(favicon.place())


from mixer.backend.django import mixer


class TestModels:

    def test_place(self):
        size = mixer.blend('mainapp.Shippet', size=0)
        assert size == 0
