#!/usr/bin/env python

import MySQLdb as mysql
import os

from flask.ext.login import UserMixin
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash


app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URL']='mysql://root:123456@127.0.0.1/flask'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@127.0.0.1/flask'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role')
    def __repr__(self):
        return 'Role {0}'.format(self.name)


class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %s>' %self.username

class Groups_form(db.Model):
    __tablename__ = "groups_form"
    groupname = db.Column(db.String(64),primary_key=True)
    def __repr__(self):
        return 'Group {0}'.format(self.groupname)


class Server_ip(db.Model):
    __tablename__ = "server_ip"
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    group = db.Column(db.String(64))
    alias = db.Column(db.String(64))
    ip = db.Column(db.String(64),primary_key=True,index=True)
    port = db.Column(db.String(64))
    user = db.Column(db.String(64))
    passwd = db.Column(db.String(64))
    def __repr__(self):
        return '{0}'.format(self.groupname)

def auth(name,passwd):
    sun=User(username=name,password=passwd,role_id=1)
    db.session.add(sun)
    db.session.commit()


if __name__ in '__mian__':
    auth('sunyang','123456')
