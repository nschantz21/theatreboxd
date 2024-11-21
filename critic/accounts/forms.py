# accounts/forms.py
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # You can add custom validation for password here (optional)
        return password
