# coding: UTF-8
from organization.models.t_custom import  CustomClass  as Custom
from organization.models.database import *


def get_custom():
    custom = Custom.query.filter.all();
    return custom


def save_custom(Custom):
        db.add(Custom)
        db.commit()

def get_by_custom_id(custom_id):
    custom = Custom.query.filter(Custom.id == custom_id).first()
    return custom