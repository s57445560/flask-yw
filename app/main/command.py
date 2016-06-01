#!/usr/bin/env python
#coding=utf8

from flask import request, render_template,session
from . import main
from flask.ext.login import login_required
import os,commands

@main.route('/command_default',methods=['GET', 'POST'])
@login_required
def command():
    print request.method
    print "1111"
    if request.method == 'POST':
        if not request.form['cmd'] == '':
            session['cmd'] = request.form['cmd']
        else:
            return render_template('command.html')
    else:
        return render_template('command.html')
    return render_template('command.html',comm=commands.getstatusoutput(session['cmd'])[1])

