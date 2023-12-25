from flask import render_template
from models.user import db

def login():
    palabra_de_bienvenida = "Bienvenido a la pagina de login"
    db.session.commit()
    return render_template('login.html', palabra_de_bienvenida=palabra_de_bienvenida)