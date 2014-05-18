# coding: utf-8

"""功能性的基类"""


class InitUpdate(object):
    """定义了初始化和更新的函数"""

    def init_value(self, args, kwargs):
        """必须初始化的值"""
        for arg in args:
            setattr(self, arg, kwargs.pop(arg))

    def init_none(self, args, kwargs):
        """选择性初始化的值，其他的初始化为None"""
        for arg in args:
            setattr(self, arg, kwargs.pop(arg, None))

    def update_value(self, args, kwargs):
        for arg in args:
            if arg in kwargs:
                setattr(self, arg, kwargs.pop(arg))