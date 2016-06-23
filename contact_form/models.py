from __future__ import unicode_literals
from django.db import models


class Contact(models.Model):
    """The Contact Class will include all the fields available on the ContactForm"""

    first_name =      models.CharField(max_length=30)
    last_name =       models.CharField(max_length=30)
    phone_number =    models.CharField(max_length=30, blank=True)
    email =           models.CharField(max_length=50)
    message =         models.TextField(default=" ")

    def __str__(self):
        return self.first_name

# Create your models here.
