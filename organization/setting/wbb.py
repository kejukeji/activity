# coding: UTF-8


# flask模块需要的配置参数
# ===============================================================
DEBUG = True  # 是否启动调试功能
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT^&556gh/ghj~hj/kh'  # session相关的密匙

# models模块需要的配置参数
# ===============================================================
#SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/organizations?charset=utf8'  # 连接的数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:203563@127.0.0.1:3306/organizations?charset=utf8'  # 连接的数据库
#SQLALCHEMY_DATABASE_URI = 'mysql://root:root@42.121.108.142:3306/organizations?charset=utf8'  # 连接的数据库
SQLALCHEMY_ECHO = True  # 是否显示SQL语句
