from django.db import models


class Snippet(models.Model):
    place = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='photo')
    date = models.DateTimeField(auto_now=True)
    size = models.PositiveIntegerField(default=0, editable=False)
