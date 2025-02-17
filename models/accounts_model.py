import MySQLdb.cursors
import hashlib
from config import Config

class AccountsModel:
    def __init__(self, mysql):
        self.mysql = mysql  # MySQL kapcsolat tárolása

    def get_by_username(self, username):
        """Lekér egy felhasználót felhasználónév alapján."""
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        return cursor.fetchone()

    def get_by_id(self, user_id):
        """Lekér egy felhasználót azonosító alapján."""
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (user_id,))
        return cursor.fetchone()

    def create_account(self, username, password, email):
        """Új felhasználói fiók létrehozása."""
        # Jelszó hashelése
        hash = password + Config.SECRET_KEY
        hash = hashlib.sha1(hash.encode())
        password_hashed = hash.hexdigest()

        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password_hashed, email))
        self.mysql.connection.commit()

    def verify_login(self, username, password):
        """Ellenőrzi a bejelentkezési adatokat."""
        account = self.get_by_username(username)
        if account:
            # Jelszó ellenőrzése
            hash = password + Config.SECRET_KEY
            hash = hashlib.sha1(hash.encode())
            password_hashed = hash.hexdigest()
            if password_hashed == account['password']:
                return account  # Visszaadja a felhasználói adatokat
        return None
