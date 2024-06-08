import pyrebase

config = {
    'apiKey': "AIzaSyANIG2bzzFtuNcPpI2aQP2gcLfMpt-Kqes",
    'authDomain': "bigsmellypoop-bf658.firebaseapp.com",
    'projectId': "bigsmellypoop-bf658",
    'storageBucket': "bigsmellypoop-bf658.appspot.com",
    'messagingSenderId': "832611219537",
    'appId': "1:832611219537:web:2107bd65ef5f3e20206070"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()





# email = 'test@gmail.com'
# password = '123123123'

# user = auth.create_user_with_email_and_password(email, password)
# print(user)

# user = auth.sign_in_with_email_and_password(email, password)
# print(user)

# info = auth.get_account_info(user['idToken'])
# print(info)