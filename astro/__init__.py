from flask import Flask



def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config)


    from astro.main.routes import main

    app.register_blueprint(main)


    return app
