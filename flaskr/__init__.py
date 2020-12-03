# https://flask.palletsprojects.com/en/1.1.x/tutorial/
import os 

from flask import Flask


def create_app(test_config=None): # What does test_config mean?
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), 
        # Does this automatically create the instance directory/folder?
        # What if the path flaskr.sqlite doesn't exist?
    )


    # Not really sure what this if else statement does
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)
    

    # ensure the instance folder exists
    # makes the instance folder/directory? But what about line 12?
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    from . import db
    db.init_app(app)


    from .import auth
    app.register_blueprint(auth.bp)
    
    return app


