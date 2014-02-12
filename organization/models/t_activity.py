# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

t_activity_table = 't_activity'


class ActivityClass(Base):
    __tablename__ = t_activity_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    date = Column(DATETIME, nullable=False)
    sponsor = Column(String(50), nullable=False)
    content = Column(String(2048), nullable=False)
    act_time = Column(String(50), nullable=False)
    address = Column(String(200), nullable=False)
    readNo = Column(Integer, nullable=True)
    shareNo = Column(Integer, nullable=True)
    password = Column(String(50), nullable=False)
