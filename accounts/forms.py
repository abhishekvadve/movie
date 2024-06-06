from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username','name','email', 'phone', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),

        }

class AuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not email or not password:
            raise forms.ValidationError('You must enter both email and password.')
        return cleaned_data
    
