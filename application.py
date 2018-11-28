from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app(**config_overrides):
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    app.config.update(config_overrides)

    db.init_app(app)

    from home.views import home_app
    from pet.views import pet_app

    app.register_blueprint(home_app)
    app.register_blueprint(pet_app)
    
    return app
