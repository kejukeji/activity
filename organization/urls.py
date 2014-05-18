# coding: UTF-8

from organization import app
from flask.ext import restful
from organization.controls.activity_control import *
from organization.controls.regist_control import *
from organization.controls.custom_control import *
from organization.controls.index import *
from organization.controls.login import *
from organization.views.login_action import login_to,register_action
from organization.restfuls.verify import *
from organization.restfuls.menu import *
from organization.views.coupon import *
from organization.restfuls.countTime import *


#定义访问control路径


api = restful.Api(app)

#定义接口路劲
# api.add_resource(ClassName, '/url')

# 手机页面
app.add_url_rule('/showactivity/<int:activity_id>', 'show_activity', show_activity)
app.add_url_rule('/renew/<int:activity_list_id>','renew',renew,methods=['GET','POST'])
app.add_url_rule('/renew_activity/<int:activity_id>','renew_activity',renew_activity,methods=['GET','POST'])
app.add_url_rule('/index', 'index', index)
app.add_url_rule('/customlist/<int:activity_id>', 'show_custom_list', show_custom_list)
app.add_url_rule('/showactivitylist', 'show_activity_list', show_activity_list)
app.add_url_rule('/createactivity', 'create_activity', create_activity)
app.add_url_rule('/regist/<int:activity_id>', 'custom_commit', custom_commit, methods=['GET', 'POST'])
app.add_url_rule('/sponactivity', 'activity_commit', activity_commit, methods=['GET', 'POST'])
app.add_url_rule('/checkpassword/<int:activity_id>', 'check_password', check_password, methods=['GET', 'POST'])
app.add_url_rule('/start/activity', 'activity_s', activity_s, methods=['GET','POST'])
app.add_url_rule('/createmenu', 'create_menu', create_menu, methods=['GET','POST'])
app.add_url_rule('/login','login',login,methods=['GET','POST'])
app.add_url_rule('/login_action','login_to',login_to,methods=['GET','POST'])
app.add_url_rule('/register','register',register,methods=['GET','POST'])
app.add_url_rule('/register_to','register_action',register_action,methods=['GET','POST'])
app.add_url_rule('/modifyactivity','modify_activity',modify_activity,methods=['GET','POST'])
app.add_url_rule('/tomodifyactivity/<int:activity_id>', 'to_modify_activity', to_modify_activity)
app.add_url_rule('/comment/<int:activity_id>', 'comment_commit', comment_commit,methods=['GET','POST'])
app.add_url_rule('/home','to_home',to_home,methods=('GET','POST'))
app.add_url_rule('/send','to_send',to_send,methods=('GET','POST'))
app.add_url_rule('/getCoupon','to_getCoupon',to_getCoupon,methods=('GET','POST'))
app.add_url_rule('/to_share','to_share',to_share,methods=('GET','POST'))
app.add_url_rule('/total','get_total_times',get_total_times,methods=('GET','POST'))

# 接口定义
api = restful.Api(app)
api.add_resource(ViewTimes,'/viewTimes')
api.add_resource(ClickTimes,'/clickTimes')
