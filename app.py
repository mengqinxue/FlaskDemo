import logging
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from database import db

# must import otherwise does not generate migrate files
from app.modules.user.module import UserModule, UserInfo

# Create a Flask object
app = create_app()

# Encapsulate app
manager = Manager(app=app)

# Establish Migrate
migrate = Migrate(app=app, db=db)

# Allow manager to operate db: python app.py db --help
# python app.py db init -> generate migrations folder
# python app.py db migrate -> generate version file
# python app.py db upgrade ->
manager.add_command('db', MigrateCommand)

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
