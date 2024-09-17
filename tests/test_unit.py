import unittest
from unittest.mock import patch

from src.app import home, app, process_registration_form


class TestHomeFunction(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    @patch('src.app.render_template')
    def test_home_content(self, mock_render_template):
        mock_render_template.return_value = "Mocked Template Response"

        # Test that the home function returns the correct content
        response = home()
        mock_render_template.assert_called_with('home.html')
        self.assertEqual(response, "Mocked Template Response")

    @patch('src.app.show_registration_form')
    def test_post_registration_data(self, mock_show_registration_form):
        # Set the mock return value to simulate successful form submission
        mock_show_registration_form.return_value = 'Welcome, Hello World!'

        # Simulate the POST request with form data
        with app.test_request_context('/register', method='POST', data={'first_name': 'Hello', 'last_name': 'World'}):
            response = app.view_functions['show_registration_form']()
            self.assertIn('Welcome, Hello World!', response)

    def test_valid_form_data(self):
        form_data = {'first_name': 'Hello', 'last_name': 'World'}
        result, error = process_registration_form(form_data)
        self.assertIsNone(error)  # There should be no error
        self.assertEqual(result['first_name'], 'Hello')
        self.assertEqual(result['last_name'], 'World')

    def test_missing_first_name(self):
        form_data = {'first_name': 'Hello', 'last_name': 'World'}
        result, error = process_registration_form(form_data)
        self.assertIsNotNone(error)  # Error should be returned
        self.assertEqual(error, "First Name and Last Name are required!")  # Check error message
        self.assertIsNone(result)  # Result should be None

    def test_missing_last_name(self):
        form_data = {'first_name': 'Hello', 'last_name': ''}
        result, error = process_registration_form(form_data)
        self.assertIsNotNone(error)
        self.assertEqual(error, "First Name and Last Name are required!")  # Check error message
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
