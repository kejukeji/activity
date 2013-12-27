# coding: UTF-8
from organization.models.t_regist import RegistClass as Regist
from organization.models.database import db


def save_regist(Regist):
    db.add(Regist)
    db.commit()


def get_by_activity_id(activity_id):
    regist_count = Regist.query.filter(Regist.activity_Id == activity_id).count()
    if regist_count ==1:
        regist = Regist.query.filter(Regist.activity_Id == activity_id).first()
    elif regist_count > 1:
        regist = Regist.query.filter(Regist.activity_Id == activity_id).all()
    else:
        regist = None
    return regist

def get_count_by_activity_id(activity_id):
    regist_count = Regist.query.filter(Regist.activity_Id == activity_id).count()
    return regist_count


