from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from blog.views import post_list

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        
        html = response.content.decode('utf8')
        #self.assertTrue(html.startswith('<html>'))
        self.assertIn("<title>Keerthi's blog</title>", html)
        #self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'blog/post_list.html')