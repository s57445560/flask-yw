#!/usr/bin/python
#coding=utf-8

from . import main
from flask import render_template
from flask.ext.login import login_required
from flask import request, flash, redirect, url_for
from flask import abort
from flask import Blueprint, render_template
from flask import request
from ..models import Groups_form, Server_ip
from .. import db
from flask_login import login_user, logout_user
from flask.ext.login import login_required

@main.route('/index')
@login_required
def index():
    group_num = Groups_form.query.count()
    ip_num = Server_ip.query.count()
    return render_template("index.html",group_num = group_num,ip_num=ip_num,zyname=u"主机信息")
