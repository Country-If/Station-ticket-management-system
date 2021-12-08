#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class management_ui:
    """管理界面"""

    def __init__(self):
        """
        实例化对象
        """
        # 动态加载界面
        qfile = QFile("ui/management.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = management_ui()
    window.ui.show()
    app.exec_()
