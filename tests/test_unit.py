import unittest
from unittest.mock import patch

from src.app import home, app, save_student, db


class TestHomeFunction(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        # Create tables
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Drop tables after the test
        with app.app_context():
            db.session.remove()
            db.drop_all()

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

    # Test when db.session.add is mocked
    @patch('src.app.db.session.add')
    @patch('src.app.db.session.commit')
    def test_post_registration_data(self, mock_commit, mock_add):
        response = self.app.post('/register', data={
            'first_name': 'Hello',
            'last_name': 'World'
        })

        # Ensure the add and commit methods were called
        mock_add.assert_called_once()
        mock_commit.assert_called_once()

        # Verify the status code and the success message
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration Successful', response.data)

    # Separate test mocking save_student instead of db calls
    @patch('src.app.save_student')
    def test_save_student_called(self, mock_save_student):
        response = self.app.post('/register', data={
            'first_name': 'Hello',
            'last_name': 'World'
        })
        mock_save_student.assert_called_once_with('Hello', 'World')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
