# coding: utf-8

import hashlib
import urllib2
import json
from .message import msg_format


class WebChat(object):
    """微信类"""

    def __init__(self, token, appid=None, secret=None):
        self.token = token
        self.appid = appid
        self.secret = secret

    def update(self, appid, secret):
        self.appid = appid
        self.secret = secret

    def validate(self, timestamp, nonce, signature):
        """验证微信接入的参数，成功返回True 否则 False"""
        hash_string = ''.join(sorted([self.token, timestamp, nonce]))
        return signature == hashlib.sha1(hash_string).hexdigest()

    def create_menu(self, menu_string):
        menu_url = self.create_menu_url()
        urllib2.urlopen(menu_url, menu_string.encode('utf-8'))

    def get_access_token(self):
        """得到access_token"""
        access_token_url = self.token_url()
        f = urllib2.urlopen(access_token_url)
        json_string = f.read()
        return json.loads(json_string)['access_token']

    def token_url(self):
        """返回获取access_token的链接"""
        return "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" \
               % (self.appid, self.secret)

    def create_menu_url(self):
        """返回创建菜单的url"""
        access_token = self.get_access_token()
        return "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + str(access_token)

    @staticmethod
    def reply(msg_type, msg_dict):
        return msg_format(msg_type, msg_dict)