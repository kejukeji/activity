# coding: UTF-8
from organization.models.t_comment import CommentClass as Comment
from organization.models.database import *
from sqlalchemy import desc


def save_comment(Comment):
    db.add(Comment)
    db.commit()

def find_comment_by_activityId(activity_Id):
    comment_count = Comment.query.filter(Comment.activity_Id==activity_Id).count()
    if comment_count == 1:
        comment = Comment.query.filter(Comment.activity_Id==activity_Id).first()
    elif comment_count > 1:
        comment = Comment.query.filter(Comment.activity_Id==activity_Id).order_by(desc(Comment.id)).all()
    else :
        comment = None
    return comment

def get_comment_count(activity_Id):
    count = Comment.query.filter(Comment.activity_Id==activity_Id).count()
    return count
