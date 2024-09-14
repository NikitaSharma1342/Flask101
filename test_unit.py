import unittest
from app import home

class TestHomeFunction(unittest.TestCase):

    def test_home_content(self):
        # Test that the home function returns the correct content
        response = home()
        self.assertEqual(response, "Welcome to the School Management System")

if __name__ == '__main__':
    unittest.main()
