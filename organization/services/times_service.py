# coding:UTF-8

from organization.models.times import Times
from organization.models.database import db



def find_by_id(id):
    return Times.query.filter(Times.id == id).first()

def updateView():
    b = find_by_id(1)
    b.view_times = b.view_times + 1
    db.commit()

def updateClick():
    b = find_by_id(1)
    b.click_times = b.click_times + 1
    db.commit()

def get_times():
    t = find_by_id(1)
    return t