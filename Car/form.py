from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email address")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,strip=False)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput,strip=False)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")