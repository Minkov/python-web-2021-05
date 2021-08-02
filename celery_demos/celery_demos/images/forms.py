from django import forms


class FileUploadForm(forms.Form):
    image_file = forms.ImageField(required=True)
