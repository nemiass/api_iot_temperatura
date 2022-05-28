from flask import Flask, jsonify
from flask_cors import CORS
from app.views.temperatura import temperatura
from app.Errors.register_error_handlers import register_error_handler


def create_app(config) -> Flask:
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(config)
    app.register_blueprint(temperatura, url_prefix="/api/temperatura")

    # registrando los handlers de errores
    register_error_handler(app)

    from app.db import db
    from app.ext import ma

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    return app
