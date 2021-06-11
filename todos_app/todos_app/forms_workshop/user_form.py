from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


def validate_name(value):
    if value[0] != value[0].upper():
        raise ValidationError('The name must start with an uppercase letter')


def validate_age(value):
    if value <= 0:
        raise ValidationError('The age cannot be less than zero.')


def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Enter a valid password')
    if any([not x.isalnum() for x in value]):
        raise ValidationError('Enter a valid password')


class UserForm(forms.Form):
    name = forms.CharField(
        validators=[
            MinLengthValidator(6),
            validate_name,
        ],
    )
    age = forms.IntegerField(
        validators=[
            validate_age,
        ],
    )
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[
            validate_password,
        ],
    )
    text = forms.CharField(
        widget=forms.Textarea(),
    )

    def clean_password(self):
        pure_password = self.cleaned_data['password']
        return f'!{pure_password}!'
