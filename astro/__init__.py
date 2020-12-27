from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
bcrypt = Bcrypt()


mail = Mail()


def create_app():
    app = Flask(__name__)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from astro.main.routes import main

    app.register_blueprint(main)


    return app
