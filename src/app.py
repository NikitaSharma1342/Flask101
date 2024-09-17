from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)


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
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        # Save student to the database
        new_student = Student(first_name=first_name, last_name=last_name)
        db.session.add(new_student)
        db.session.commit()

        return render_template('registration_success.html', first_name=first_name, last_name=last_name)

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
