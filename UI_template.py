#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class ui:
    """***"""

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
        qfile = QFile("***.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)


if __name__ == '__main__':
    Connect = pymysql.connect(host='localhost', user='root', password='root', database='ticket_management_system',
                              port=3306)
    Cursor = Connect.cursor()

    app = QApplication(sys.argv)
    window = ui(Connect, Cursor)
    window.ui.show()
    app.exec_()

    Cursor.close()
    Connect.close()
