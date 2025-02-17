from flask import Flask, request
from flask_mysqldb import MySQL
from config import Config
from controllers.auth_controller import AuthController
from controllers.register_controller import RegisterController
from controllers.home_controller import HomeController
from controllers.profile_controller import ProfileController

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)  # Inicializáljuk a MySQL kapcsolatot

# Kontroller példányosítás
auth_controller = AuthController(mysql)

@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    return auth_controller.login(request)

@app.route('/pythonlogin/logout')
def logout():
    return auth_controller.logout()

@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    return RegisterController(mysql).register(request)

@app.route('/pythonlogin/home')
def home():
    return HomeController().home()

@app.route('/pythonlogin/profile')
def profile():
    return ProfileController(mysql).profile()