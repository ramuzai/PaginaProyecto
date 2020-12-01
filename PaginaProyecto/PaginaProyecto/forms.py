from django.forms import ModelForm
from django import forms

class ContactoForm(forms.Form):
	mensaje = forms.CharField(widget=forms.Textarea)
	correo = forms.EmailField()