#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class query_result_ui:
    """登录前的查询结果界面"""

    def __init__(self, connect_obj, cursor):
        """
        实例化对象

        :param connect_obj: 数据库连接对象
        :param cursor: 数据库游标对象
        """
        # 获取数据库连接
        self.connect_obj = connect_obj
        self.cursor = cursor

        # 动态加载界面
        qfile = QFile("query_result.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

    def change_information(self, date, departure, destination):
        """
        修改标签

        :param date: 日期
        :param departure: 始发站
        :param destination: 终点站
        :return: None
        """
        self.ui.date_chosen.setText(date)
        self.ui.departure_label.setText(departure)
        self.ui.destination_label.setText(destination)


if __name__ == '__main__':
    Connect = pymysql.connect(host='localhost', user='root', password='root', database='ticket_management_system',
                              port=3306)
    Cursor = Connect.cursor()

    app = QApplication(sys.argv)
    window = query_result_ui(Connect, Cursor)
    window.change_information('2021-12-1', '广州', '深圳')
    window.ui.show()
    app.exec_()

    Cursor.close()
    Connect.close()
