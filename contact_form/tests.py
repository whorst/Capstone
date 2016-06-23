# -*- coding: utf-8 -*-
from django.test import TestCase

from models import Contact

class EncodingTestCase(TestCase):
    """Tests that a unicode character that is saved to the database is the same when it's returned from the database."""

    def test_encoding_is_proper(self):
        test_str = u"✄"
        name = Contact(first_name=test_str)
        name.save()
        name2 = Contact.objects.get(first_name=test_str)
        self.assertEqual(name.first_name, name2.first_name)
