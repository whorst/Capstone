from __future__ import unicode_literals

from django.db import models
from time import strftime


class Announcement(models.Model):
#The Announcement Model will appear on the home.html page

    title = models.CharField(max_length=90)
    description = models.TextField(default = " ")
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
