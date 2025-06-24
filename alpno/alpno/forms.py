# app1/forms.py
from django import forms

class MyForm(forms.Form):
    # Add your form fields here
    name = forms.CharField(label='Hammad', max_length=100)
    email = forms.EmailField(label='haha@gmai;.com')