from flask import Flask

from app.core.routes import member_blueprint
from app.extensions import db, migrate


def blueprint_register(app):
    app.register_blueprint(member_blueprint)


app = Flask(__name__)
app.config.from_object("configs.Config")

db.init_app(app)
blueprint_register(app)

migrate.init_app(app, db)
