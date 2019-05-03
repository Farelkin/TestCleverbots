from mixer.backend.django import mixer


class TestModels:

    def test_place(self):
        size = mixer.blend('size.Shippet')
        assert size == 0
