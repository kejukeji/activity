__author__ = 'Juingya'
#coding: UTF-8
from flask import request,render_template,flash
from organization.models.t_user import query,add,query_mobile
def login_to():
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    if query(mobile,password):
         return  render_template('index.html')
    else:
         flash(u'用户名或密码错误，请检查并重试！')
         return render_template('login.html')

def register_action():
    name = request.form.get('username')
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    repassword = request.form.get('repassword')
    if password == repassword:
       if query_mobile(mobile):
           flash(u'该手机已注册，直接登录')
           return render_template('login.html')
       else:
            #添加到数据库
           if add(name,mobile,password):
               flash('注册成功')
               return render_template('login.html')

    else:
           flash('密码不一致，请重新填写')
           return render_template('register.html')

