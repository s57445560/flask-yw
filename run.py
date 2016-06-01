#!/usr/bin/env python

from app import create_app
from flask.ext.sqlalchemy import SQLAlchemy
from app.models import User,Role
from flask.ext.script import Manager

app = create_app()

app.run(debug=True,host='0.0.0.0',port=99,threaded=True)
#manager = Manager(app)

#@manager.command
#def test():
#    print "1112"
#
#manager.run()

