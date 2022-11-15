from dataclasses import field
from django import forms
from .models import *

class Search(forms.Form):
    polling_unit = forms.CharField(max_length=300,required=True)
    

