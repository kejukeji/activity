# coding: UTF-8

from flask import request,render_template
from organization.services.activity_service import *
from datetime import datetime
from organization.services.regist_service import *
from organization.services.custom_service import *
from organization.controls.custom_control import *
from organization.restfuls.verify import *
import hashlib

def show_activity(activity_id):
    activity = get_activity(activity_id)
    activity.readNo = activity.readNo + 1
    save_activity(activity)
    regist_result = get_by_activity_id(activity_id)
    regist_count = get_count_by_activity_id(activity_id)
    regist_list = []
    if regist_result == None:
        massage = '目前还没有人参加，欢迎参加！'
    elif type(regist_result) is list:
        for regist in regist_result:
            custom_result = get_by_custom_id(regist.custom_Id)
            custom_result.send_date = regist.send_date
            regist_list.append(custom_result)
    else:
        custom_result = get_by_custom_id(regist_result.custom_Id)
        custom_result.send_date = regist_result.send_date
        regist_list.append(custom_result)
    content_url = url(activity_id)

    return render_template('/showactivity.html',
                           activity = activity,
                           regist_list = regist_list,
                           regist_count = regist_count,
                           content_url = content_url
                            )

def activity_commit():
    if request.method == 'POST':
        Activity = html_activity(request.form)
        Activity.readNo = 1
        save_activity(Activity)
        add_sponsor(Activity.sponsor, Activity.id)


        #return show_activity(Activity.id)
        return redirect(url_for("show_activity", activity_id=Activity.id))

def to_modify_activity(activity_id):
    activity = get_activity(activity_id)
    return render_template('modifyactivity.html',activity = activity)

def modify_activity():
    if request.method == 'POST':
        Activity = html_modify_activity(request.form)
        activity = get_activity(Activity.id)
        activity.title = Activity.title
        activity.content = Activity.content
        activity.act_date = Activity.act_date
        activity.act_time = Activity.act_time
        activity.address = Activity.address
        activity.date = str(datetime.now())
        save_activity(activity)
        return redirect(url_for("show_activity", activity_id = activity.id))



def html_modify_activity(form):
    return Activity(id = form.get('id'),
                    title = form.get('title'),
                    content = form.get('content'),
                    act_date = form.get('act_date'),
                    act_time = form.get('act_time'),
                    address = form.get('address')
                    )

def add_sponsor(sponsor, activity_id):
        Custom = html_custom(request.form, sponsor)
        save_custom(Custom)

        RegistDb = Regist(custom_Id = Custom.id,
                          activity_Id = activity_id,
                          send_date = str(datetime.now()))
        save_regist(RegistDb)
        return None
def html_custom(form, sponsor):
    return Custom(name = sponsor,
                   mobile = form.get('inputMobile'))

def html_activity(form):
    dateformat = str(datetime.now())
    return Activity(title = form.get('title'),
                    content = form.get('content'),
                    sponsor = form.get('sponsor'),
                    act_date = form.get('act_date'),
                    act_time = form.get('act_time'),
                    address = form.get('address'),
                    password = hashlib.new('md5', form.get('password')).hexdigest(),
                    date = dateformat)


def show_activity_list():
    activity_list = get_activity_list()
    activity_count = get_activity_count()
    return render_template('showactivitylist.html',
                           activity_count = activity_count,
                           activity_list = activity_list)

def check_password(activity_id):
    password_html = hashlib.new('md5', request.form.get('passwordcheck')).hexdigest()
    password = find_pass_by_id(activity_id)
    if password == password_html:
        return show_custom_list(activity_id)
    else:
        error_message = '对不起，密码错误！'
        return render_template('error.html',
                               error_message = error_message,
                               activity_id = activity_id)

def create_activity():
    return render_template('createactivity.html')
def renew(activity_list_id):
    activity = get_activity(activity_list_id)
    password_html = hashlib.new('md5', request.form.get('passwordcheck')).hexdigest()
    password = find_pass_by_id(activity_list_id)
    if password == password_html:
       return render_template('renew.html',activity = activity)
    else:
        error_message = '对不起，密码错误无权修改！'
        return render_template('error.html',
                               error_message = error_message,
                               activity_id = activity_list_id)

def renew_activity(activity_id):
    title = request.form.get('title')
    time = request.form.get('time')
    address = request.form.get('address')
    content = request.form.get('content')
    activity = get_activity(activity_id)
    activity.title = title
    activity.act_time = time
    activity.address = address
    activity.content = content
    save_activity(activity)
    return redirect(url_for("show_activity", activity_id=activity.id))



