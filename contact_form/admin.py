from django.contrib import admin

from models import Contact
import forms
# Register your models here.


class ContactForm(forms.ModelForm):
    """This class will render the form from our Model and all the necessary fields."""

    class Meta:

        model = Contact
        fields = "__all__"

    def clean_email(self):
        """Checks to make sure that submitted emails are in the proper format."""
        email = self.cleaned_data["email"]
        if "@" not in email:
            raise forms.ValidationError("Not an Email Address")
        return email


class ContactAdmin(admin.ModelAdmin):
    """The ContactAdmin class will simply display our Announcement Model's fields on the Admin page, but not the user page."""

    form = ContactForm

admin.site.register(Contact, ContactAdmin)
