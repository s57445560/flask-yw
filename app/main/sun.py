#!/usr/bin/python
#coding=utf-8

from . import main
from werkzeug.routing import BaseConverter
from flask.ext.login import login_required
from flask import render_template

class RegexConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex=items[0]


@main.route('/config')
@login_required
def sun():
    return render_template('config.html',zyname=u"主机与组配置信息")
