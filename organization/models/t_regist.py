# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base
from .t_custom import CustomClass
from .t_activity import ActivityClass

t_regist_table = 't_regist'


class RegistClass(Base):
    __tablename__ = t_regist_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    custom_Id = Column(Integer, ForeignKey(CustomClass.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    activity_Id = Column(Integer, ForeignKey(ActivityClass.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    send_date = Column(DATETIME, nullable=False)
