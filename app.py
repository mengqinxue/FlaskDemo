import logging
from flask_script import Manager

from app import create_app


# Create a Flask object
app = create_app()

# Encapsulate app
manager = Manager(app=app)


# python app.py upgrade
@manager.command
def init():
    print('Initialize server')


@manager.command
def upgrade():
    print('Upgrade server')


if __name__ == '__main__':
    # Start a WSGI server and 0.0.0.0 allows to request externally
    manager.run()
