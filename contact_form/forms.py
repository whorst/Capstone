from models import Contact
import forms


class ContactForm(forms.ModelForm):


    class Meta:
        Model = Contact
        fields = "__all__"
