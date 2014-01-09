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
    Content = xml_recv.find("Content").text
    input_type = get_type(Content)

    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text
    reply_dict = {
        "ToUserName": FromUserName,
        "FromUserName": ToUserName,
        "Content": input_type
    }
    return response(web_chat, reply_dict, "text")

def response_event(xml_recv, web_chat):
    #Event = xml_recv.find("Event").text
    #EventKey = xml_recv.find("EventKey").text
    activity_id = string.atoi(xml_recv.find("Content").text)
    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text

    #if (Event == 'CLICK') and (EventKey == 'story'):
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


BASE_URL = "http://bilibili.kejukeji.com"

def url(activity_id):
    return BASE_URL+"/showactivity/"+str(activity_id)