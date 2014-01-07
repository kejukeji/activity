# coding: UTF-8
from organization.models.t_activity import ActivityClass as Activity
from organization.models.database import *

def get_activity(act_id):
    activity = Activity.query.filter(Activity.id == act_id).first()
    return activity

def get_activity_count():
    activity_count = Activity.query.filter().count()
    return activity_count

def get_activity_list():
    activity_count = Activity.query.filter().count()
    if activity_count ==1 :
        activity_list = Activity.query.filter().first()
    elif activity_count > 1:
        activity_list = Activity.query.filter().all()
    else:
        activity_list = None
    return activity_list


def save_activity(Activity):
    db.add(Activity)
    db.commit()


def find_pass_by_id(activity_id):
    activity = Activity.query.filter(Activity.id == activity_id).first()
    return activity.password
