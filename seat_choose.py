#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class seat_choose_ui:
    """座位选择界面"""

    def __init__(self):
        """
        实例化对象
        """

        # 动态加载界面
        qfile = QFile("ui/seat_choose.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)
        self.result = ""

    def get_result(self, result):
        self.result = result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = seat_choose_ui()
    window.ui.show()
    app.exec_()
