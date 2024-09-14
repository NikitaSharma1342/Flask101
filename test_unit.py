import unittest
from unittest.mock import patch
from app import home

class TestHomeFunction(unittest.TestCase):

    @patch('app.render_template')
    def test_home_content(self,mock_render_template):
        mock_render_template.return_value = "Mocked Template Response"

        # Test that the home function returns the correct content
        response = home()
        mock_render_template.assert_called_with('home.html')
        self.assertEqual(response, "Mocked Template Response")

if __name__ == '__main__':
    unittest.main()
