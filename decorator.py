#!/env/Scripts python
# @File    : decorator.py
# @Time    : 2018/11/20 20:17
# @Author  : Bb
# -*- coding: utf-8 -*-

from functools import wraps
from flask import session,redirect,url_for

#登录限制
def login_required(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper
