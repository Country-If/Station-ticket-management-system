#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class query_ui:
    """查询界面"""

    def __init__(self):
        """
        实例化对象
        """
        # 动态加载界面
        qfile = QFile("ui/query.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)
        self.ui.date_chosen.setDate(QDate.currentDate())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = query_ui()
    window.ui.show()
    app.exec_()
