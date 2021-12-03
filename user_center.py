#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class user_center_ui:
    """用户中心界面"""

    def __init__(self):
        """
        实例化对象
        """

        # 动态加载界面
        qfile = QFile("ui/user_center.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

    def set_username(self, username):
        """
        设置用户名

        :param username: 用户名
        :return: None
        """
        self.ui.username_label.setText(username)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Username = "测试"
    window = user_center_ui()
    window.set_username(Username)
    window.ui.show()
    app.exec_()
