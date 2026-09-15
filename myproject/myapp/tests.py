from django.test import TestCase


class HomeTest(TestCase):
    def test_home(self):
        self.assertEqual(2 + 2, 4)


class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)


class HomeContentTest(TestCase):
    def test_home_content(self):
        response = self.client.get('/aboutus/')
        self.assertContains(response, "About Us")

















