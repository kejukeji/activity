# coding:UTF-8

from .database import Base
from .base_class import InitUpdate
from sqlalchemy import Column, String, Integer, ForeignKey, FLOAT
from sqlalchemy.dialects.mysql import DOUBLE

TIMES = 'times'

class Times(Base, InitUpdate):
    '''用户'''
    __tablename__ = TIMES
    id = Column(Integer, primary_key=True)
    view_times = Column(Integer,nullable=True)
    click_times = Column(Integer,nullable=True)