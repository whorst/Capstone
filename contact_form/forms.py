from models import Contact
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms


class ContactForm(ModelForm):


    class Meta:
        model = Contact
        fields = "__all__"


    def clean_email(self):
        email = self.cleaned_data["email"]

        if "@" not in email:
            print("OOOOOOooOoOooOOOOoOoooooOOOOOoooOOOooooooOoooOOOsss")
            raise ValidationError("Not an Email Address")

        return email
