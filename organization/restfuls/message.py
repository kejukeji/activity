# coding: utf-8

import time

TEXT = """
<xml>
<ToUserName><![CDATA[$ToUserName$]]></ToUserName>
<FromUserName><![CDATA[$FromUserName$]]></FromUserName>
<CreateTime>$CreateTime$</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[$Content$]]></Content>
<FuncFlag>0</FuncFlag>
</xml>
"""

NEWS_HEAD = """
<xml>
<ToUserName><![CDATA[$ToUserName$]]></ToUserName>
<FromUserName><![CDATA[$FromUserName$]]></FromUserName>
<CreateTime>$CreateTime$</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>$ArticleCount$</ArticleCount>
<Articles>
"""
NEWS_ITEM = """
<item>
<Title><![CDATA[$Title$]]></Title>
<Description><![CDATA[$Description$]]></Description>
<PicUrl><![CDATA[$PicUrl$]]></PicUrl>
<Url><![CDATA[$Url$]]></Url>
</item>
"""
NEWS_TAIL = """
</Articles>
<FuncFlag>1</FuncFlag>
</xml>
"""


def msg_format(msg_type, msg_dict):
    """返回格式化的xml"""
    if msg_type == 'text':  # text
        return msg(msg_dict, TEXT)
    if msg_type == 'news':  # text picture
        return msg_news(msg_dict)


def msg(msg_dict, xml_string):
    """返回文字消息的xml"""
    msg_dict["CreateTime"] = str(int(time.time()))
    for k in msg_dict:
        xml_string = xml_string.replace('$'+k+'$', msg_dict[k])
    return xml_string


def msg_news(msg_dict):
    """返回一个图文消息的xml"""
    msg_dict["CreateTime"] = str(int(time.time()))
    xml_string = NEWS_HEAD
    for k in msg_dict:
        xml_string = xml_string.replace('$'+k+'$', str(msg_dict[k]))

    for item in msg_dict["item"]:
        xml_string += msg(item, NEWS_ITEM)

    return xml_string + NEWS_TAIL