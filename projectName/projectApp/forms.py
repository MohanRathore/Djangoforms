from django import forms
from .models import GeekModel

class InputForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(initial="Negi")
    email = forms.EmailField()
    available = forms.BooleanField()

class GeekForm(forms.ModelForm):
    class Meta:
        model = GeekModel
        fields = "__all__"
        # exclude = ['title']