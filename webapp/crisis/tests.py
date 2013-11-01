"""
Filename : crisis/tests.py
Authors : Seshagiri Prabhu
Copyright : Wise Earth Technology
Credits : Bithin Alangot
This file is part of the CrisisCommunicator Project ...
It is licensed under the Peaceful Open Source License...
Please see the License terms in the PeaceOSL.txt
-
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
