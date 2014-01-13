# coding: utf-8


from flask import make_response, request
from xml.etree import ElementTree as ET
from .webchat import WebChat
from .tools import *
import string


def activity_s():
    web_chat = WebChat('1234')
    if request.method == "GET":
        if web_chat.validate(**parse_request(request.args, ("timestamp", "nonce", "signature"))):
            return make_response(request.args.get("echostr"))
        raise LookupError

    if request.method == "POST":
        xml_recv = ET.fromstring(request.data)
        MsgType = xml_recv.find("MsgType").text

        if MsgType == "text":
            return response_text(xml_recv, web_chat)
        if MsgType == "event":
            return response_event(xml_recv, web_chat)

def response(web_chat, reply_dict, reply_type):
    reply = web_chat.reply(reply_type, reply_dict)
    reply_response = make_response(reply)
    reply_response.content_type = 'application/xml'
    return reply_response


def get_type(Content):
    if 'u' in Content:
        return "http://bilibili.kejukeji.com/index"
    if Content.startswith("fa"):
        return "gai"


def response_text(xml_recv, web_chat):
    content = xml_recv.find("Content").text
    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text

    if content == 'h':
        message = HELP
        reply_dict = {
            "ToUserName": FromUserName,
            "FromUserName": ToUserName,
            "Content":message
        }
        return response(web_chat, reply_dict, "text")
    elif content == 'my':
        message = 'http://bilibili.kejukeji.com/createmenu'
        reply_dict = {
            "ToUserName": FromUserName,
            "FromUserName": ToUserName,
            "Content":message
        }
        return response(web_chat, reply_dict, "text")
    elif content == 'c':
         reply_dict = {
            "ToUserName": FromUserName,
            "FromUserName": ToUserName,
            "ArticleCount": 1,
            "item": [{
                "Title": '创建活动',
                "Description": "点击进入创建活动页面",
                "PicUrl": BASE_URL+'/static/image/huodong1.jpg',
                "Url": BASE_URL+"/index"
            }]
         }
         return response(web_chat, reply_dict, "news")
    else:
        activity_id = string.atoi(content)
        activity = get_activity_weixin(activity_id)
        reply_dict = {
            "ToUserName": FromUserName,
            "FromUserName": ToUserName,
            "ArticleCount": 1,
            "item": [{
                "Title": str(activity.title),
                "Description": str(activity.content),
                "PicUrl": BASE_URL+'/static/image/huodong1.jpg',
                "Url": url(activity_id)
            }]
        }
        return response(web_chat, reply_dict, "news")

def response_event(xml_recv, web_chat):
    Event = xml_recv.find("Event").text
    EventKey = xml_recv.find("EventKey").text
    activity_id = string.atoi(xml_recv.find("Content").text)
    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text
    if (Event == 'CLICK') and (EventKey == 'viewActivity'):
        reply_dict = {
            "ToUserName": FromUserName,
            "FromUserName": ToUserName,
            "ArticleCount": 1,
            "item": [{
                "Title": '查看活动',
                "Description": "点击进入活动列表",
                "PicUrl": BASE_URL+'/static/image/huodong1.jpg',
                "Url": BASE_URL+"/showactivitylist"
            }]
         }
        return response(web_chat, reply_dict, "news")




BASE_URL = "http://bilibili.kejukeji.com"
HELP = "感谢关注客聚科技活动平台，输入'h'获取帮助信息，输入'my'获取我参与的活动，输入'c'创建一个新活动!"

def url(activity_id):
    return BASE_URL+"/showactivity/"+str(activity_id)