from django import forms
from django.contrib.auth.models import User
from django.forms import CharField


class RegisterForm(forms.ModelForm):
    password = CharField(widget=forms.PasswordInput, max_length=50)
    password_confirm = CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta():
        model = User
        fields = ["username", "password", "password_confirm"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Your password doesn't match")

        return cleaned_data
