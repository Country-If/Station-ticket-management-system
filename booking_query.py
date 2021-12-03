#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class booking_query_ui:
    """订单查询界面"""

    def __init__(self):
        """
        实例化对象
        """

        # 动态加载界面
        qfile = QFile("ui/booking_query.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

    def setUsername(self, username):
        self.ui.username_label.setText(username)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Username = "测试"
    window = booking_query_ui()
    window.setUsername(Username)
    window.ui.show()
    app.exec_()
