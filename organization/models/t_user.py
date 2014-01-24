# coding: utf-8

from sqlalchemy import Column, Integer, String
from .database import Base


t_user_table = 't_user'


class UserClass(Base):
    __tablename__ = t_user_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    mobile = Column(String(30), nullable=False)
    password = Column(String(6),nullable=False)
def query(mobile,password):
    user =  UserClass.query.filter(UserClass.mobile==mobile,UserClass.password==password)
    if user:
        return True
    else:
        return False

