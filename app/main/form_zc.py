#!/usr/bin/python
#coding=utf8

from . import main
from flask import request, flash, redirect, url_for
from flask import abort
from flask import render_template
from flask import Blueprint, render_template
from flask import request
from ..models import Groups_form, Server_ip
from .. import db
from flask_login import login_user, logout_user
from flask.ext.login import login_required

@main.route('/form/group',methods=['GET', 'POST'])
@login_required
def group():
    print request.method
    if request.method == 'POST':
        user = Groups_form.query.filter_by(groupname=unicode(str(request.form['group_form']),"utf-8")).first()
        print user
        if user is None and request.form['group_form'] != "":
            groups_id = Groups_form(groupname=unicode(str(request.form['group_form']).rstrip(),"utf-8"))
            db.session.add(groups_id)
            db.session.commit()
            a=request.form['group_form']
            print a
            flash(u'添加成功!')
        else:
            flash(u'重复的主机名，请重新输入')
    return render_template('form/group.html')


@main.route('/form/user',methods=['GET', 'POST'])
@login_required
def user():
    group_id = Groups_form.query.all()
    if request.method == 'POST':
       ip_id = Server_ip.query.filter_by(ip=unicode(request.form['user_ip'])).first() 
       if ip_id is None:
           mydb = Server_ip(group=unicode(str(request.form['group_id']),"utf-8"),alias=unicode(str(request.form['user_c']),"utf-8"),ip=request.form['user_ip'],port=request.form['user_p'],user=request.form['user_u'],passwd=request.form['user_d'])
           db.session.add(mydb)
           db.session.commit()
           flash(u'添加成功!')
       else:
          flash(u'重复的主机名，请重新输入')
    return render_template('form/user.html',group_id=group_id)

