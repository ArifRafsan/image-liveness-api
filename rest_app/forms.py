from django import forms
#from upload_validator import FileTypeValidator
from django.core.validators import FileExtensionValidator


class UserForm(forms.Form):
    # Field for creating file input
    file = forms.FileField(validators=[FileExtensionValidator(['mp4', 'MP4'])])


