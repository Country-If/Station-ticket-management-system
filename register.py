#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class register_ui:
    def __init__(self, connect_obj, cursor):
        self.connect_obj = connect_obj
        self.cursor = cursor
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

        sql = r"insert into user_information(user_name, password, target) values('%s', '%s', '%s');" \
              % (username, password, '0')
        try:
            self.cursor.execute(sql)
            self.connect_obj.commit()
            QMessageBox.information(self.ui, '注册成功', '请前往登录界面')
            self.clear()
        except Exception as e:
            QMessageBox.critical(self.ui, '注册失败', str(e))
            self.connect_obj.rollback()

    def clear(self):
        self.ui.username_label.clear()
        self.ui.password_label.clear()
        self.ui.confirm_label.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = register_ui()
    window.ui.show()
    app.exec_()
