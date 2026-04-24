from django import forms
from .models import Movie
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter movie title...'}),
            'year': forms.NumberInput(attrs={'placeholder': 'e.g. 2024', 'min': 1900, 'max': 2030}),
            'description': forms.Textarea(attrs={'placeholder': 'Write a short description...', 'rows': 4}),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'