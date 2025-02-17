from flask import session, redirect, url_for, render_template

class HomeController:
    def home(self):
        if 'loggedin' in session:
            return render_template('home.html', username=session['username'])
        return redirect(url_for('login'))