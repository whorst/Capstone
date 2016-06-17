from django.contrib import admin
from django.core.exceptions import ValidationError

from models import Announcement
import forms

import re


class AnnouncementForm(forms.ModelForm):
#This class will render the form from our Model and all the necessary fields.


    class Meta:
#Meta class is used to contain extra information about the model that would not
#necessarily be appropriate to contain within the model class itself.

        model = Announcement
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if (bool(re.match(r"[\w ]{3,}$", title)) == False):
            raise ValidationError("Your title isn't long enough")
        return title


class AnnouncementAdmin(admin.ModelAdmin):
#The AdminModelForm class will simply display our Announcement Model's fields on the Admin page, but not the user page.

    form = AnnouncementForm


admin.site.register(Announcement, AnnouncementAdmin)
