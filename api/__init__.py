from flask import Flask
from flask_migrate import Migrate
from config import Config
from .extensions import api, db
from .resources import api as ns_api
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.config.from_object(Config)

    db.init_app(app)
    api.init_app(app)
    api.add_namespace(ns_api)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()
    return app
