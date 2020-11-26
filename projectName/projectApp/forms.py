from django import forms

class InputForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    available = forms.BooleanField()