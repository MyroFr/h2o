from flask import Flask, session, render_template, request, redirect
import pyrebase

app = Flask(__name__)


config = {
    'apiKey': "AIzaSyANIG2bzzFtuNcPpI2aQP2gcLfMpt-Kqes",
    'authDomain': "bigsmellypoop-bf658.firebaseapp.com",
    'projectId': "bigsmellypoop-bf658",
    'storageBucket': "bigsmellypoop-bf658.appspot.com",
    'messagingSenderId': "832611219537",
    'appId': "1:832611219537:web:2107bd65ef5f3e20206070",
    'databaseURL': ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'


@app.route('/', methods=['GET', 'POST'])
def index():
    if('user' in session):
        return 'Hi, {}'.format(session['user'])
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
            return 'Thank you for login'
        except:
            return 'Failed to login'
    else:
        return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = email
            return 'Thank you for register'
        except:
            return 'Failed to register'
    else:
        return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


if __name__ == "__main__":
    app.run()