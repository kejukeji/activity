# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

t_custom_table = 't_custom'


class CustomClass(Base):
    __tablename__ = t_custom_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    mobile = Column(String(30), nullable=False)
    openId = Column(String(50), nullable=True)