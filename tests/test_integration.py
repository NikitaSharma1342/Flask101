import unittest
from src.app import app, db, Student


class TestHomePage(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory database for testing
        self.app = app.test_client()

        # Push the app context to avoid "working outside of application context" error
        self.app_context = app.app_context()
        self.app_context.push()

        db.create_all()  # Create all tables

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        # Pop the app context after the tests
        self.app_context.pop()

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

    def test_get_registration_form(self):
        # Simulate a GET request to '/register'
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)  # The page should load successfully
        self.assertIn(b'<form', response.data)  # Check if a form is present in the response
        self.assertIn(b'First Name', response.data)  # Check for a field called 'First Name'
        self.assertIn(b'Last Name', response.data)  # Check for a field called 'Last Name'

    def test_post_registration_form(self):
        # Simulate a POST request to '/register' with student data
        response = self.app.post('/register', data={
            'first_name': 'Hello',
            'last_name': 'World'
        })
        self.assertEqual(response.status_code, 200)  # Ensure the POST request is successful
        self.assertIn(b'Registration Successful', response.data)  # Ensure success message is shown

        # Verify that the student is saved in the database
        student = Student.query.filter_by(first_name='Hello', last_name='World').first()
        self.assertIsNotNone(student)  # Ensure student is in the database
        self.assertEqual(student.first_name, 'Hello')
        self.assertEqual(student.last_name, 'World')


if __name__ == '__main__':
    unittest.main()
