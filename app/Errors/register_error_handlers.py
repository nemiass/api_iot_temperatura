from flask import Flask, jsonify
from marshmallow import ValidationError


def register_error_handler(app: Flask):
    @app.errorhandler(Exception)
    def handle_exception_error(e: Exception):
        return jsonify({
            "message": "Internal Server Error",
            "details": str(e)
        }), 500


    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return jsonify({
            "message": "Json incorrect format",
            "details": str(e)
        }), 400
