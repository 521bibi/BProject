#!/env/Scripts python
# @File    : exts.py
# @Time    : 2018/11/15 21:41
# @Author  : Bb
# -*- coding: utf-8 -*-
import os

DEBUG = True

# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '741123'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'Bdata'

SQLALCHEMY_DATABASE_URI =  "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE,)
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'

SECRET_KEY = os.urandom(24)
