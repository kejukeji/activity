from flask import make_response, request
from xml.etree import ElementTree as ET
from .webchat import WebChat
from .tools import get_token


def activity_s(open_id):
    web_chat = WebChat()
    if request.method == "GET":
        raise LookupError

    if request.method == "POST":
        xml_recv = ET.fromstring(request.data)
        MsgType = xml_recv.find("MsgType").text

        if MsgType == "text":
            return response_text(xml_recv, web_chat)

def response(web_chat, reply_dict, reply_type):
    reply = web_chat.reply(reply_type, reply_dict)
    reply_response = make_response(reply)
    reply_response.content_type = 'application/xml'
    return reply_response


def get_type(Content):
    if Content.startswith("fa"):
        return "jia"
    if Content.startswith("fa"):
        return "gai"


def response_text(xml_recv, web_chat):
    Content = xml_recv.find("Content").text
    input_type = get_type(Content)

    reply_dict = {
        "ToUserName": '',
        "FromUserName": '',
        "Content": Content,
        "item": [{
                "Title": str(''),
                "Description": str(''),
                "Url": 'activity_url'
            }]
    }
    return response(web_chat, reply_dict, "text")