from django import forms
from django.forms import ModelForm
from .models import Something

class NameForm(forms.Form):
  your_name = forms.CharField(label='Your name', max_length=100)

class Norm(ModelForm):
  class Meta:
    model=Something
    fields=['some_key','pub_date']

