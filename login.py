#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class login_ui:
    """登录界面"""

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
        qfile = QFile("login.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login_ui()
    window.ui.show()
    app.exec_()
