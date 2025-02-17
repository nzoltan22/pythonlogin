from flask import render_template
import re
from models.accounts_model import AccountsModel

class RegisterController:
    def __init__(self, mysql):
        self.accounts_model = AccountsModel(mysql)

    def register(self, request):
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']

            account = self.accounts_model.get_by_username(username)

            if account:
                msg = 'Account already exists!'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers!'
            elif not username or not password or not email:
                msg = 'Please fill out the form!'
            else:
                self.accounts_model.create_account(username, password, email)
                msg = 'You have successfully registered!'
        elif request.method == 'POST':
            msg = 'Please fill out the form!'

        return render_template('register.html', msg=msg)
    