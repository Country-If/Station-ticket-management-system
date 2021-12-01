#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class login_ui:
    """登录界面"""

    def __init__(self):
        """
        实例化对象
        """
        # 动态加载界面
        qfile = QFile("ui/login.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login_ui()
    window.ui.show()
    app.exec_()
