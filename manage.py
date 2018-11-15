#!/env/Scripts python
# @File    : exts.py
# @Time    : 2018/11/15 21:41
# @Author  : Bb
# -*- coding: utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app
from exts import db

manager = Manager(app)

#绑定app,db
migrate = Migrate(app,db)
#迁移命令
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()