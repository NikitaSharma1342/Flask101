import unittest
from src.app import app

class TestHomePage(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home_page(self):
        # Simulate a GET request to the home page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Welcome to the School Management System</h1>', response.data)  # Check for the welcome message

    def test_home_page_content_type(self):
        response = self.app.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')  # Check content type

    def test_home_page_title(self):
        response = self.app.get('/')
        self.assertIn(b'<title>Home</title>', response.data)  # Check that the title is present


if __name__ == '__main__':
    unittest.main()
