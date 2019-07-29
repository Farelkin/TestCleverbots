from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils.six import BytesIO
from PIL import Image
from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient

# def create_image(storage, filename, size=(150, 150), image_mode='RGB', image_format='PNG'):
#    data = BytesIO()
#    Image.new(image_mode, size).save(data, image_format)
#    data.seek(0)
#    if not storage:
#        return data
#    image_file = ContentFile(data.read())
#    return storage.save(filename, image_file)
#
#
# class UploadImageTests(TestCase):
#
#     def setUp(self):
#         super(UploadImageTests, self).setUp()
#
#     def test_valid_form(self):
#         avatar = create_image(None, 'malevich_square.png')
#         avatar_file = SimpleUploadedFile('malevich_square.png', avatar.getvalue())
#         data = {'place': 'test place', 'image': avatar_file}
#         response = self.client.post('/service/photo/', data, follow=True)
#         self.assertEquals(response.status_code, 201)


class TestGetRequest(TestCase):

    # def test_get_request(self):
    #     response = self.client.get('service/photos/1/')
    #     self.assertEqual(response.status_code, 200)

    def test_get_request_REST(self):
        response = self.client.get('/service/photos/1')
        self.assertEqual(response.data, {"place": "home",
                                            "image": "http://127.0.0.1:8000/media/photo/favicon.png",
                                            "date": "2019-04-16T14:36:12.623999Z",
                                            "size": 4789})
