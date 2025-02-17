from flask import session, redirect, url_for, render_template
from models.accounts_model import AccountsModel

class ProfileController:
    def __init__(self, mysql):
        self.accounts_model = AccountsModel(mysql)

    def profile(self):
        if 'loggedin' in session:
            account = self.accounts_model.get_by_id(session['id'])
            return render_template('profile.html', account=account)
        return redirect(url_for('login'))
