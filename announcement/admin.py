from django.contrib import admin
from django.core.exceptions import ValidationError
from models import Announcement
import forms

import re

class AdminModelForm(admin.ModelAdmin):
#The AdminModelForm class will simply display our Announcement Model's fields on the Admin page, but not the user page.

    class Meta:
        model = Announcement
        fields = "__all__"

    def clean(self):
        print("Hello")
        title = self.cleaned_data.get('title')
        if (bool(re.match(r'[\w ]{3,}$', title)) == False):
            raise ValidationError("Your title isn't long enough")
        return title

admin.site.register(Announcement, AdminModelForm)
