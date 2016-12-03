import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from main import app, db

APP_SETTINGS="config.DevelopmentConfig"
app.config.from_object(APP_SETTINGS)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()