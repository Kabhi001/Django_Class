from django.test import TestCase

# Create your tests here.

class HomeTest(TestCase):
    def test_home(self):
        self.assertEqual(2+2,4)
