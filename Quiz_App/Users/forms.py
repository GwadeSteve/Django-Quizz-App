from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'sex', 'course_program', 'major', 'level', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username *'
        self.fields['email'].label = 'Email Address *'
        self.fields['sex'].label = 'Gender *'
        self.fields['course_program'].label = 'Course Program *'
        self.fields['major'].label = 'Major *'
        self.fields['level'].label = 'Academic Level *'
        self.fields['password1'].label = 'Create Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters.'

class CustomUserLoginForm(forms.Form):
    username = forms.CharField(label='Full Name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
