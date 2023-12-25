# Importing the necessary modules and libraries
from flask import Flask
from flask_migrate import Migrate
from routes.user_route import blueprint
from models.user import db



def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    db.init_app(app)  # Initializing the database
    return app


app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint)
# migrate = Migrate(app, db)  # Initializing the migration

if __name__ == '__main__':
    app.run(debug=True)