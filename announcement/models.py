from __future__ import unicode_literals

from django.db import models
from time import strftime


class Announcement(models.Model):
#The Announcement Model will appear on the home.html page

    title = models.CharField(max_length=90)
    description = models.TextField(default=" ")
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
'''
Test if a unicode character saved to the database is still a unicode character when it's returned.
Create a new announcement test object that has a unicode character in it. Save that object to the database
(using save override?) and then grab it from the database and check it agains the original object.
(using save override?) and then grab it from the database and check it agains the original object.
'''

'''
Create a Contact Us form that checks if an email address exists.
https://docs.djangoproject.com/en/dev/ref/forms/fields/
'''
