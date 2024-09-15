from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Registration route (GET)
@app.route('/register', methods=['GET', 'POST'])
def show_registration_form():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        return render_template('registration_success.html', first_name=first_name, last_name=last_name)
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
