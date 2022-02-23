# flaskr/__init__.py

import os

from flask import Flask

from .core import limiter  # <------- New line

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    limiter.init_app(app) # <--------------------------------- New line

    if  test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # a simple endpoint that says hello
    @app.route('/test')
    def hello():
        return 'Hello, World!'
    
    # register the blueprint
    from . import resource
    app.register_blueprint(resource.bp)

    return app