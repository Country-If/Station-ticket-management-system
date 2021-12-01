#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *


class register_ui:
    """注册界面"""

    def __init__(self, connect_obj, cursor):
        """
        实例化对象

        :param connect_obj: 数据库连接对象
        :param cursor: 数据库游标对象
        """
        # 获取数据库连接
        self.connect_obj = connect_obj
        self.cursor = cursor

        # 动态加载界面
        qfile = QFile("ui/register.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)

        # 信号与槽连接
        self.ui.confirm_label.returnPressed.connect(self.register)
        self.ui.register_btn.clicked.connect(self.register)

    def register(self):
        """
        注册函数

        :return: None
        """
        # 获取输入框文本
        username = self.ui.username_label.text()
        password = self.ui.password_label.text()
        confirm_passwd = self.ui.confirm_label.text()

        # 对输入信息进行检查
        if username == '':
            QMessageBox.critical(self.ui, '错误', '用户名不能为空')
        elif password == '':
            QMessageBox.critical(self.ui, '错误', '密码不能为空')
        elif confirm_passwd == '':
            QMessageBox.critical(self.ui, '错误', '确认密码不能为空')
        elif password != confirm_passwd:
            QMessageBox.critical(self.ui, '错误', '两次输入的密码不同！')
        else:
            # 执行SQL语句
            sql = r"insert into user_information(user_name, password, target) values('%s', '%s', '%s');" \
                  % (username, password, '0')
            try:
                self.cursor.execute(sql)
                self.connect_obj.commit()
                QMessageBox.information(self.ui, '注册成功', '请前往登录界面')
                self.clear()
            except Exception as e:
                err_print(self.ui, e)
                self.connect_obj.rollback()

    def clear(self):
        """
        清空文本框

        :return: None
        """
        self.ui.username_label.clear()
        self.ui.password_label.clear()
        self.ui.confirm_label.clear()


if __name__ == '__main__':
    Connect = pymysql.connect(host='localhost', user='root', password='root', database='ticket_management_system',
                              port=3306)
    Cursor = Connect.cursor()

    app = QApplication(sys.argv)
    window = register_ui(Connect, Cursor)
    window.ui.show()
    app.exec_()

    Cursor.close()
    Connect.close()
