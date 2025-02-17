from flask import session, redirect, url_for, render_template
from models.accounts_model import AccountsModel

class AuthController:
    def __init__(self, mysql):
        self.accounts_model = AccountsModel(mysql)

    def login(self, request):
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']

            account = self.accounts_model.verify_login(username, password)

            if account:
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                return redirect(url_for('home'))
            else:
                msg = 'Incorrect username/password!'
        return render_template('index.html', msg=msg)

    def logout(self):
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)
        return redirect(url_for('login'))
    