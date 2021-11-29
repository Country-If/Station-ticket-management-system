#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"


from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import sys


class register_ui:
    def __init__(self):
        qfile = QFile("register.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        self.ui = QUiLoader().load(qfile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = register_ui()
    window.ui.show()
    app.exec_()
