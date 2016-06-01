#!/usr/bin/env python

from __init__ import create_app
from flask.ext.sqlalchemy import SQLAlchemy

app = create_app()
db = SQLAlchemy(app)

app.run(debug=True,host='0.0.0.0',port=99,threaded=True)

