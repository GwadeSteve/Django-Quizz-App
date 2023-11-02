# forms.py
from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'op1', 'op2', 'op3', 'op4', 'answer']
