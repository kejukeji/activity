__author__ = 'Juingya'
#coding: UTF-8
from flask import request,render_template,flash
from organization.models.t_user import query
def login_to():
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    if query(mobile,password):
       return  render_template('index.html')
    else:
        flash(u'用户名或密码错误，请检查并重试！')
        return render_template('login.html')