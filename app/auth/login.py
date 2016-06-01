#!/usr/bin/env python
#coding=utf8

from flask import request, flash, redirect, url_for
from flask import abort
from flask import render_template
from flask import Blueprint, render_template
from flask import request
from . import auth
from ..models import User
from .. import db
from flask_login import login_user, logout_user
from flask.ext.login import login_required



@auth.route('/login',methods=['GET', 'POST'])
def login():
    print request.method
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['user']).first()
        if user is not None and  user.verify_password(request.form['passwd']):
            login_user(user)
            return render_template("index.html",name=request.form['user'])
        else:
            flash(u'确认用户名密码是否正确!')

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.')
    return redirect(url_for('auth.login'))

