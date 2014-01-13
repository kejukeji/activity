# coding: utf-8

from flask import flash
from .webchat import WebChat
from .cons_string import MENU_STRING


def create_menu():
    web_chat = WebChat('1234')
    web_chat.update('wx1426988e8c227dee', 'a9e807647ac0b5b5ef1fe6e5b1c7e3ce')
    menu_string = render_string(MENU_STRING)

    try:
        web_chat.create_menu(menu_string)
    except:
        flash(u"创建微信菜单失败，由于网速的问题会有偶尔的失败")


def render_string(menu_string):
    url = "http://bilibili.kejukeji.com/"
    return menu_string.replace("$url$", url)