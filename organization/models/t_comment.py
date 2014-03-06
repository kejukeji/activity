# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base
from .t_activity import ActivityClass

t_comment_table = 't_comment'


class CommentClass(Base):
    __tablename__ = t_comment_table

    __table_args__ = {
       'mysql_engine': 'InnoDB',
       'mysql_charset': 'utf8'
    }

    id = Column(Integer, primary_key=True)
    activity_Id = Column(Integer, ForeignKey(ActivityClass.id, ondelete='cascade', onupdate='cascade'), nullable=False)
    comment = Column(String(300), nullable=True)