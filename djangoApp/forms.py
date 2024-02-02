from django import forms
from .models import Submission

class MyForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['name','email','message']
