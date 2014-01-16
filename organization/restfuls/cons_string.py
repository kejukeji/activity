# coding: utf-8

"""定义回复的常量"""

MENU_STRING = """
{
   "button": [
       {
           "name": "活动主页",
           "sub_button": [
               {
                   "type":"view",
                   "name": "发起活动",
                   "url":"http://bilibili.kejukeji.com/createactivity"
               },
               {
                   "type":"view",
                   "name": "查看活动",
                   "url":"http://bilibili.kejukeji.com/showactivitylist"
               }
           ]
       },
       {
           "name": "趣味活动",
           "sub_button": [
               {
                   "type": "click",
                   "name": "抽奖",
                   "key": "prize"
               },
               {
                   "type": "click",
                   "name": "刮刮",
                   "key": "scrape"
               }
           ]
       },
       {
           "type": "click",
           "name": "我的活动",
           "key": "myActivity"
       }
   ]
}
"""

ALREADY_BIND = "您之前已经是酒吧会员。绑定的号码为：MOBILE。如果需要修改绑定的手机号码，输入 gai手机号，比如 gai1872191xx24"
BIND_ERROR_FORMAT = "成为酒吧会员，请输入正确的格式，比如 jia1872191xx24"
CHANGE_ERROR_FORMAT = "修改绑定手机号，请输入正确的格式，比如 gai1872191xx24"
NOT_BIND = "您还不是酒吧会员，输入 jia手机号 进行微信绑定，比如 jia1872191xx24"
BIND_SUCCESS = "您已经是酒吧会员了，微信绑定的手机号为：MOBILE。感谢您的加入！"
CHANGE_SUCCESS = "您成功修改了手机号，新绑定的手机号为：MOBILE。感谢您的加入！"
CHANGE_NONE = "您还未成为会员，成为酒吧会员，请输入正确的格式，比如 jia1872191xx24"
ALREADY_EXIST = "手机号MOBILE已经被其他微信号绑定"
NO_ACTIVITY = "目前没有优惠活动"
NO_GIFT = "很抱歉，您没有中奖。"
HAS_GIFT = "恭喜你，中奖了！"
NOT_USER_GIFT = "抱歉，酒吧会员才能抽奖哦。"
HAS_ROLL = "一天只能抽奖一次哦。让我们期待美好的明天吧 ~"
NORMAL_REPLY = "系统没能理解您的意思，通过菜单操作更方便哦 ~"
NOT_VALID_PUB = "本酒吧微信服务暂时关闭，很抱歉对您造成不便。"