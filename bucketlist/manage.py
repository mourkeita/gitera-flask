#! /usr/bin/python
# coding: utf8

import os

from app import models
from app import db, create_app

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

appli =  create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(appli, db)
manager = Manager(appli)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()