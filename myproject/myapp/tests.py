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


class GradeCalcTest(TestCase):
    def test_grade_calc_page(self):
        response = self.client.get('/grade/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grade.html')
        self.assertEqual(response.context['name'], 'Anurag')
        self.assertEqual(response.context['marks'], 40)
        self.assertContains(response, 'Grade: Average')

























