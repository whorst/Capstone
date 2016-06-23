from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms

from models import Contact

class ContactForm(ModelForm):
    """This will produce the form (using a ModelForm) for our contact_form"""

    class Meta:
        model = Contact
        fields = "__all__"

    def clean_email(self):
        """Checks to make sure that submitted emails are in the proper format."""
        email = self.cleaned_data["email"]
        if "@" not in email:
            raise ValidationError("Not an Email Address")
        return email
