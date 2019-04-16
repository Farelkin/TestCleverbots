from django import forms


class UploadFileForm(forms.Form):
    place = forms.CharField(max_length=50)
    file = forms.ImageField()
