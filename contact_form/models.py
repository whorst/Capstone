from __future__ import unicode_literals
from django.db import models


class Contact(models.Model):
    """The Contact Class will include all the fields available on the ContactForm"""

    first_name =      models.CharField(max_length=30)
    last_name =       models.CharField(max_length=30)
    phone_number =    models.CharField(max_length=12)
    email =           models.EmailField(blank=False)
    message =         models.TextField(default=" ", blank=False)

    def __str__(self):
        return self.first_name

# Create your models here.
