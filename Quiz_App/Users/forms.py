from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'sex', 'course_program', 'major', 'level', 'password1', 'password2']

    name = forms.CharField(label='Full Name *', max_length=150)
    email = forms.EmailField(label='Email Address *')
    sex = forms.ChoiceField(label='Gender *', choices=[('', 'Select Gender')] + CustomUser.GENDER, initial='', required=True)
    course_program = forms.ChoiceField(label='Course Program *', choices=[('', 'Select Course')] + CustomUser.COURSES, initial='', required=True)
    major = forms.CharField(label='Major *', max_length=100, initial='', required=True)
    level = forms.ChoiceField(label='Academic Level *', choices=[('', 'Select Level')] + CustomUser.LEVELS, initial='', required=True)
    password1 = forms.CharField(label='Create Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

class CustomUserLoginForm(forms.Form):
    name = forms.CharField(label='Full Name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
