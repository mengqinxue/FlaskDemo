from flask import Flask, Response

from database import db
from app.modules.user import user_bp
from app.configs.web_config import DevelopmentConfig


# services
functions = {'s1': 'generate_feature', 's2': 'train', 's3': 'predict'}


# wrap up app function initialization
def create_app():
    # Initialize a Flask server.
    app = Flask(__name__)
    # print(app.template_folder) app and templates should be in the same folder

    # Load server configuration
    app.config.from_object(DevelopmentConfig)

    # Database mapping
    db.init_app(app=app)

    # Register blueprint
    app.register_blueprint(user_bp)

    @app.route('/', endpoint='index')
    def index():
        return Response('Index Page')

    # pass a string
    @app.route('/services/<service>')
    def service(service):
        return functions.get(service)

    # pass a number: int/float
    @app.route('/add/<int:n1>/<int:n2>')
    def add(n1, n2):
        return str(n1 + n2)

    # pass a UUID
    @app.route('/test/<uuid:id>')
    def redirect():
        return str('id' + str(5))

    #
    print(app.url_map)

    # Return configured Flask app object
    return app
