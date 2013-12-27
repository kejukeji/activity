# coding: UTF-8

from organization.services.custom_service import *
from organization.services.regist_service import *
from organization.controls.activity_control import *
from datetime import datetime
from flask import request, render_template, redirect, url_for


def custom_commit(activity_id):

    if request.method =='POST':
        Custom = html_custom(request.form, activity_id)
        save_custom(Custom)

        RegistDb = Regist(custom_Id = Custom.id,
                      activity_Id = activity_id,
                      send_date = str(datetime.now()))
        save_regist(RegistDb)
        return redirect(url_for("show_activity", activity_id=activity_id))


def html_custom(form, activity_id):
    return Custom(name= form.get('inputName'),
                 mobile= form.get('inputMobile'))


def show_custom_list(activity_id):
    regist_result = get_by_activity_id(activity_id)
    regist_count = get_count_by_activity_id(activity_id)
    regist_list = []
    if regist_result == None:
        massage = '目前还没有人参加，欢迎参加！'
    elif type(regist_result) is list:
        for regist in regist_result:
            custom_result = get_by_custom_id(regist.custom_Id)
            regist_list.append(custom_result)
    else:
        custom_result = get_by_custom_id(regist_result.custom_Id)
        regist_list.append(custom_result)


    return render_template('/customlist.html',
                           regist_list = regist_list,
                           regist_count = regist_count)

