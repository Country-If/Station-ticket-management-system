#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class main_ui:
    def __init__(self):
        qfile = QFile("main.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        self.ui = QUiLoader().load(qfile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_ui()
    window.ui.show()
    app.exec_()
