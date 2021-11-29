#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

import pymysql
from sshtunnel import SSHTunnelForwarder

if __name__ == '__main__':
    # 通过SSH连接云服务器
    server = SSHTunnelForwarder(
        ssh_address_or_host=('120.79.14.209', 22),  # 云服务器地址IP和端口port
        ssh_username='mysql_db',  # 云服务器登录账号
        ssh_password='mysql_db',  # 云服务器登录密码
        remote_bind_address=('localhost', 3306)  # 数据库服务地址ip,一般为localhost和端口port，一般为3306
    )
    # 云服务器开启
    server.start()
    # 云服务器上mysql数据库连接
    connect_obj = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                                  port=server.local_bind_port,
                                  user='stms',  # mysql的登录账号
                                  password='stms',  # mysql的登录密码
                                  db='ticket_management_system',  # mysql中要访问的数据库
                                  charset='utf8')  # 表的字符集
    # 创建游标
    cursor = connect_obj.cursor()

    sql = r"show tables;"

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except Exception as e:
        print(e)
        cursor.rollback()

    # 断开连接
    cursor.close()
    connect_obj.close()
    server.close()
