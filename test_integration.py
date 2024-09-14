import unittest
from app import app

class TestHomePage(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home_page(self):
        # Simulate a GET request to the home page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the School Management System', response.data)  # Check for the welcome message


if __name__ == '__main__':
    unittest.main()
