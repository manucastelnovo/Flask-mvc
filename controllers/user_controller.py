from flask import render_template


def login():
    palabra_de_bienvenida = "Bienvenido a la pagina de login"
    return render_template('login.html', palabra_de_bienvenida=palabra_de_bienvenida)