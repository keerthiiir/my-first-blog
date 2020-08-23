from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
import blog.views


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        
        html = response.content.decode('utf8')
        self.assertIn("<title>Keerthi's blog</title>", html)

        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_uses_Postedit_template(self):
        response = self.client.get('/post/new/')
        self.assertTemplateUsed(response, 'blog/post_edit.html')

    def test_uses_CV_template(self):
        response = self.client.get('/CV/')
        self.assertTemplateUsed(response, 'blog/CVpost_list.html')

    def test_uses_CVedit_template(self):
        response = self.client.get('/CV/new/')
        self.assertTemplateUsed(response, 'blog/CVpost_edit.html')
