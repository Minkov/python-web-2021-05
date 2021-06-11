from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator


def validate_dot(value_to_validate):
    if '.' in value_to_validate:
        raise forms.ValidationError('\'.\' is present in value')


def validate_bot_catcher_empty(value):
    if value:
        raise ValidationError('You are a bot')


#
# def validate_min_length(min_length):
#     def validate(value):
#         if len(value) < min_length:
#             raise forms.ValidationError
#
#     return validate


class CreateTodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        validators=[
            validate_dot,
            MinLengthValidator(3),
            # validate_min_length(5),
        ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter todo text',
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-text-area',
                'rows': 3,
            }
        )
    )

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
        validators=[
            # validate_bot_catcher_empty,
        ]
    )

    def clean_bots_catcher(self):
        value = self.cleaned_data['bots_catcher']
        validate_bot_catcher_empty(value)


class UpdateTodoForm(CreateTodoForm):
    state = forms.BooleanField()
