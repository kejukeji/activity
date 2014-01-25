# coding: UTF-8

from sqlalchemy import Column, Integer, String
from .database import Base,db


t_user_table = 't_user'


class UserClass(Base):
    __tablename__ = t_user_table


    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    mobile = Column(String(30), nullable=False)
    password = Column(String(6),nullable=False)
def query(mobile,password):
    user = UserClass.query.filter(UserClass.mobile == mobile,UserClass.password == password).first()
    if user:
        return True
    else:
        return False
def add(name,mobile,password):
    user = UserClass(name = name, mobile= mobile,password=password)
    db.add(user)
    try:
        db.commit()
    except:
        return False
    return True
def query_mobile(mobile):
    user = UserClass.query.filter(UserClass.mobile == mobile).first()
    if user:
        return True
    else:
        return False







