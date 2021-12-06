import os
from flask import Flask
from .builder import *

def create_app():
    template_dir = os.path.abspath('templates')
    app = Flask(__name__, template_folder=template_dir)

    from . import server
    app.register_blueprint(server.bp)

    return app

Person.load_data_from_json()

Post.load_post_from_json()
