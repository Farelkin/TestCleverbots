from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils.six import BytesIO
from PIL import Image


def create_image(storage, filename, size=(150, 150), image_mode='RGB', image_format='PNG'):
   data = BytesIO()
   Image.new(image_mode, size).save(data, image_format)
   data.seek(0)
   if not storage:
       return data
   image_file = ContentFile(data.read())
   return storage.save(filename, image_file)


class UploadImageTests(TestCase):

    def setUp(self):
        super(UploadImageTests, self).setUp()

    def test_valid_form(self):
        avatar = create_image(None, 'avatar.png')
        avatar_file = SimpleUploadedFile('favicon.png', avatar.getvalue())
        data = {'place': 'test place', 'image': avatar_file}
        response = self.client.post('/service/photos/', data, follow=True)
        self.assertEquals(response.status_code, 201)


class TestGetRequest(TestCase):

    def test_get_request(self):
        response = self.client.get('/service/photos/')
        self.assertEqual(response.status_code, 200)
