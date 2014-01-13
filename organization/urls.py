# coding: UTF-8

from organization import app
from flask.ext import restful
from organization.controls.activity_control import *
from organization.controls.regist_control import *
from organization.controls.custom_control import *
from organization.controls.index import *
from organization.restfuls.verify import *
from organization.restfuls.menu import *


#定义访问control路径


api = restful.Api(app)

#定义接口路劲
# api.add_resource(ClassName, '/url')

# 手机页面
app.add_url_rule('/showactivity/<int:activity_id>', 'show_activity', show_activity)
app.add_url_rule('/index', 'index', index)
app.add_url_rule('/customlist/<int:activity_id>', 'show_custom_list', show_custom_list)
app.add_url_rule('/showactivitylist', 'show_activity_list', show_activity_list)
app.add_url_rule('/regist/<int:activity_id>', 'custom_commit', custom_commit, methods=['GET', 'POST'])
app.add_url_rule('/sponactivity', 'activity_commit', activity_commit, methods=['GET', 'POST'])
app.add_url_rule('/checkpassword/<int:activity_id>', 'check_password', check_password, methods=['GET', 'POST'])
app.add_url_rule('/start/activity', 'activity_s', activity_s, methods=['GET','POST'])