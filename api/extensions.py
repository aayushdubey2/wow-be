from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

api = Api()
db = SQLAlchemy()
migrate = Migrate()