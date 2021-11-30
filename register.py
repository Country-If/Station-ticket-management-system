#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class register_ui:
    def __init__(self):
        qfile = QFile("register.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        self.ui = QUiLoader().load(qfile)

        self.ui.confirm_label.returnPressed.connect(self.register)
        self.ui.register_btn.clicked.connect(self.register)

    def register(self):
        username = self.ui.username_label.text()
        password = self.ui.password_label.text()
        confirm_passwd = self.ui.confirm_label.text()

        if username == '':
            QMessageBox.critical(self.ui, '错误', '用户名不能为空')
        elif password == '':
            QMessageBox.critical(self.ui, '错误', '密码不能为空')
        elif confirm_passwd == '':
            QMessageBox.critical(self.ui, '错误', '确认密码不能为空')
        elif password != confirm_passwd:
            QMessageBox.critical(self.ui, '错误', '两次输入的密码不同！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = register_ui()
    window.ui.show()
    app.exec_()
