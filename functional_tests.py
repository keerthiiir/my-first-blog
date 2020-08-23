from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_Postpage(self):  
        self.browser.get('http://localhost:8000')
        self.assertIn("Keerthi's blog", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn("Welcome to Keerthi's blog", header_text)
    
    def test_Posteditpage(self):  
        self.browser.get('http://localhost:8000/post/new')
        self.assertIn("Keerthi's blog", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn("New post", header_text)

    def test_CVpage(self):
        self.browser.get('http://localhost:8000/CV/')
        self.assertIn("Keerthi's blog", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn("Keerthi's CV", header_text)

    def test_CVeditpage(self):
        self.browser.get('http://localhost:8000/CV/new')
        self.assertIn("Keerthi's blog", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn("New CV Post", header_text)

if __name__ == '__main__':  
    unittest.main(warnings='ignore')