from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class ContactForm(forms.Form):

    name = forms.CharField(label="Nombre", required=True, min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, min_length=3, max_length=100)
    phone = PhoneNumberField(null=False, blank=False)
    content = forms.CharField(label="Contenido", required=True, min_length=10, max_length=1000)