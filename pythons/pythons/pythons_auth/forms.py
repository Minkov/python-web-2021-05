from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email",)


class SignInForm(AuthenticationForm):
    user = None

    def clean_password(self):
        super().clean()
        self.user = authenticate(
            email=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password incorrect')

    def save(self):
        return self.user
