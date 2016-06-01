#!/usr/bin/env python
#coding=utf8
from flask import request ,render_template
from flask.ext.login import login_required
from . import main
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = 'static/bak'

@main.route('/upload',methods=['GET','POST'])
@login_required
def upload():
    print request.method
    if request.method == 'POST':
        f = request.files['file_upload']
        fname = secure_filename(f.filename)
        f.save(os.path.join(UPLOAD_FOLDER,fname))
        print os.path.join(UPLOAD_FOLDER,fname)
        uname=u"成功"
        print fname
        return render_template('upload.html',return_f=uname)
    elif request.method == "GET":
        return render_template('upload.html')

