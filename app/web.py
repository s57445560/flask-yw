#!/usr/bin/env python

import MySQLdb as mysql
from flask.ext.login import UserMixin
from __init__ import login_manager
from __init__ import db
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__,template_folder = 'templates',static_folder = 'static',)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Role(UserMixin,db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role')

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    passwd = db.Column(db.String(128))
    role_id = db.relationship(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %s>' %self.username






@login_manager.user_loader
def load_user(user_id):
    print user_id
    return User.query.get(int(user_id))
