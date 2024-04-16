from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import portfolio

    app.register_blueprint(portfolio.bp)

    return app