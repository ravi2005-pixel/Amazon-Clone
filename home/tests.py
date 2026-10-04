from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.staticfiles import finders

class AmazonCloneViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_status_and_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_navbar_elements_present(self):
        response = self.client.get(reverse('index'))
        content = response.content.decode()
        self.assertIn('amazon', content)
        self.assertIn('.in', content)
        self.assertIn('Deliver to', content)
        self.assertIn('India', content)
        self.assertIn('Search Amazon', content)
        self.assertIn('EN ▾', content)
        self.assertIn('Hello, sign in', content)
        self.assertIn('Account & Lists ▾', content)
        self.assertIn('Returns', content)
        self.assertIn('& Orders', content)
        self.assertIn('Cart', content)

    def test_secondary_navbar_items_present(self):
        response = self.client.get(reverse('index'))
        content = response.content.decode()
        self.assertIn('Today\'s Deals', content)
        self.assertIn('Customer Service', content)
        self.assertIn('Registry', content)
        self.assertIn('Gift Cards', content)
        self.assertIn('Sell', content)

    def test_footer_sections_present(self):
        response = self.client.get(reverse('index'))
        content = response.content.decode()
        self.assertIn('Back to top', content)
        self.assertIn('Get to Know Us', content)
        self.assertIn('Make Money with Us', content)
        self.assertIn('Amazon Payment Products', content)
        self.assertIn('Let Us Help You', content)
        self.assertIn('Careers', content)
        self.assertIn('About Us', content)
        self.assertIn('Conditions of Use', content)
        self.assertIn('Privacy Notice', content)

    def test_static_files_found(self):
        css_file = finders.find('home/css/style.css')
        self.assertIsNotNone(css_file)

        js_file = finders.find('home/js/script.js')
        self.assertIsNotNone(js_file)
