from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Helper function to process the form data
def process_registration_form(form_data):
    first_name = form_data.get('first_name')
    last_name = form_data.get('last_name')
    if not first_name or not last_name:
        return None, "First Name and Last Name are required!"
    return {'first_name': first_name, 'last_name': last_name}, None


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def show_registration_form():
    error = None
    if request.method == 'POST':
        form_data, error = process_registration_form(request.form)
        if error:
            # If validation fails, pass the error to the template
            return render_template('register.html', error=error)

        # If validation passed, render the success template
        return render_template('registration_success.html', first_name=form_data['first_name'],
                               last_name=form_data['last_name'])

    # Render the registration form without any error initially
    return render_template('register.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
