# coding: UTF-8
from flask.ext import restful
from flask.ext.restful import reqparse
from organization.services.times_service import *

class ViewTimes(restful.Resource):

    @staticmethod
    def get():
        updateView()

class ClickTimes(restful.Resource):

    @staticmethod
    def get():
        updateClick()