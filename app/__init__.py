#!/usr/bin/env python
#coding=utf8

from flask.ext.login import LoginManager
from werkzeug.routing import BaseConverter
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy(use_native_unicode="utf8")

class RegexConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex=items[0]


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
#login_manager.login_message = u"没有登录请先登录"

def create_app():
    app = Flask(__name__,template_folder = 'templates',static_folder = 'static',)
    app.url_map.converters['regex'] = RegexConverter
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@127.0.0.1/flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    login_manager.init_app(app)
    db.init_app(app)

    from auth import auth
    from main import main

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


    @app.template_filter('sunyang')
    def reverse_filter(s):
        if s == 'sunyang':
            return u"大神你好！"
        else:
            return s

    return app



