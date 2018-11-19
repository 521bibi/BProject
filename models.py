#!/env/Scripts python
# @File    : exts.py
# @Time    : 2018/11/15 21:41
# @Author  : Bb
# -*- coding: utf-8 -*-
from exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    telephone = db.Column(db.String(11),nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
