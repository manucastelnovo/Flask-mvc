from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.user_route import blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'chupetess'
app.register_blueprint(blueprint)

db = SQLAlchemy(app)






