from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Registration route (GET)
@app.route('/register', methods=['GET'])
def show_registration_form():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
