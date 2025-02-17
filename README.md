# Bejelentkezési rendszer Python Flask és MySQL segítségével

Arra kerestem megoldást, hogy hogyan lehet Pythonban Flask keretrendszerrel objektumorientáltan, MVC alkalmazásával, MySQL adatbázissal webes alkalmazásokat létrehozni.  
Mivel interneten csak részmegoldásokat találtam, így ezek felhasználásával készítettem el ezt az alkalmazást.

## Funkciók

Az alkalmazás a következőket tudja:
- Regisztráció
- Bejelentkezés
- A regisztrációkor megadott adatok megtekintése

## Követelmények

- **Python 3.x**
- **MySQL**
- Telepítve legyen a **Python Flask** és **Flask-MySQLdb** csomag

## Telepítés Linuxon

Virtuális környezet létrehozása és aktiválása:

```bash
python3 -m venv venv
source venv/bin/activate  
```

Sükséges csomagok telepítése:

```bash
pip install flask
pip install flask-mysqldb
```

Az alkalmazás futtatása:

```bash
export FLASK_APP=main.py
export FLASK_DEBUG=1
flask run
```

## Az alkalmazás elérhetősége

Az elkészült program a következő linken próbálható ki:  
[https://www.eeeeee.rrrrr/ggggg](https://www.eeeeee.rrrrr/ggggg)

