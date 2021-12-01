#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tool import *
from main_ui import main_ui
from register import register_ui
from login import login_ui
from query import query_ui
from query_result import query_result_ui
from query_result_login import query_result_login_ui


class Main:
    def __init__(self, connect_obj, cursor):
        """
        实例化对象

        :param connect_obj: 数据库连接对象
        :param cursor: 数据库游标对象
        """
        self.connect_obj = connect_obj
        self.cursor = cursor
        self.login_status = False  # 登录状态
        self.username = ""  # 用户名

        # 加载所有界面
        self.main_ui = main_ui()
        self.register_ui = register_ui(self.connect_obj, self.cursor)
        self.login_ui = login_ui()
        self.query_ui = query_ui()
        self.query_result_ui = query_result_ui(self.connect_obj, self.cursor)
        self.query_result_login_ui = query_result_login_ui(self.connect_obj, self.cursor)

        # 信号与槽连接
        self.main_ui.ui.register_btn.clicked.connect(self.main_to_register)
        self.main_ui.ui.login_btn.clicked.connect(self.main_to_login)
        self.main_ui.ui.query_btn.clicked.connect(self.main_to_query)

        self.register_ui.ui.back_btn.clicked.connect(self.register_back)

        self.login_ui.ui.back_btn.clicked.connect(self.login_back)
        self.login_ui.ui.password_label.returnPressed.connect(self.login)
        self.login_ui.ui.login_btn.clicked.connect(self.login)

        self.query_ui.ui.back_btn.clicked.connect(self.query_back)
        self.query_ui.ui.query_btn.clicked.connect(self.query)

        self.query_result_login_ui.ui.back_btn.clicked.connect(self.query_result_login_back)
        self.query_result_login_ui.ui.logout_btn.clicked.connect(self.logout)

        self.query_result_ui.ui.back_btn.clicked.connect(self.query_result_back)
        self.query_result_ui.ui.login_btn.clicked.connect(self.query_result_to_login)
        self.query_result_ui.ui.register_btn.clicked.connect(self.query_result_to_register)

    def main_to_register(self):
        """
        主界面前往注册界面

        :return: None
        """
        self.main_ui.ui.close()
        self.register_ui.ui.show()

    def register_back(self):
        """
        注册界面返回

        :return: None
        """
        self.register_ui.ui.close()
        self.main_ui.ui.show()

    def main_to_login(self):
        """
        主界面前往登录界面

        :return: None
        """
        self.main_ui.ui.close()
        self.login_ui.ui.show()

    def login_back(self):
        """
        登录界面返回

        :return: None
        """
        self.login_ui.ui.close()
        self.main_ui.ui.show()

    def login(self):
        """
        登录函数

        :return: None
        """
        # 获取输入框文本
        self.username = self.login_ui.ui.username_label.text()
        password = self.login_ui.ui.password_label.text()

        # 对输入信息进行检查
        if self.username == '':
            QMessageBox.critical(self.login_ui.ui, '错误', '用户名不能为空')
        elif password == '':
            QMessageBox.critical(self.login_ui.ui, '错误', '密码不能为空')
        else:
            # 执行SQL语句
            sql = r"select * from user_information where user_name='%s' and password='%s'" \
                  % (self.username, password)
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                # 判断是否有该数据
                if len(result) != 0:
                    # 清空文本框
                    self.login_ui.ui.username_label.clear()
                    self.login_ui.ui.password_label.clear()
                    QMessageBox.information(self.login_ui.ui, '成功', '登录成功')
                    self.login_status = True
                    # 切换界面
                    self.login_ui.ui.close()
                    self.query_ui.ui.show()
                else:
                    QMessageBox.critical(self.login_ui.ui, '登录失败', '用户名或密码错误')
            except Exception as e:
                err_print(self.login_ui.ui, e)

    def main_to_query(self):
        self.main_ui.ui.close()
        self.query_ui.ui.show()

    def query_back(self):
        self.query_ui.ui.close()
        self.main_ui.ui.show()

    def query(self):
        # 获取输入框文本
        departure = self.query_ui.ui.departure_label.text()
        destination = self.query_ui.ui.destination_label.text()
        date = self.query_ui.ui.date_chosen.text()

        # 对输入信息进行检查
        if departure == '' and destination == '':
            QMessageBox.critical(self.query_ui.ui, '错误', '始发站和终点站不能为空')
        elif departure == '':
            self.query_departure(destination)
        elif destination == '':
            self.query_destination(departure)
        else:
            self.query_check(departure, destination, date)

    def query_departure(self, destination):
        sql = r"select distinct departure from train_information where destination='%s';" % destination
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if len(result) == 0:
                QMessageBox.critical(self.query_ui.ui, '错误', '查询不到相关信息，请重新输入终点站')
            else:
                QMessageBox.information(self.query_ui.ui, '提示', '可选始发站为：' + str([d[0] for d in result]))
        except Exception as e:
            err_print(self.query_ui.ui, e)

    def query_destination(self, departure):
        sql = r"select distinct destination from train_information where departure='%s';" % departure
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if len(result) == 0:
                QMessageBox.critical(self.query_ui.ui, '错误', '查询不到相关信息，请重新输入始发站')
            else:
                QMessageBox.information(self.query_ui.ui, '提示', '可选终点站为：' + str([d[0] for d in result]))
        except Exception as e:
            err_print(self.query_ui.ui, e)

    def query_check(self, departure, destination, date):
        # 查询始发站和终点站是否有日期信息
        sql = r"select date from train_information where departure='%s' and destination='%s';" % (
        departure, destination)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if len(result) == 0:
                QMessageBox.critical(self.query_ui.ui, '错误', '查询不到信息，请重新输入')
            else:
                if datetime.date(*map(int, date.split('/'))) in [d[0] for d in result]:
                    QMessageBox.information(self.query_ui.ui, '提示', '查询成功')
                    # 根据登录状态切换界面
                    self.query_ui.ui.close()
                    if self.login_status:
                        self.query_result_login_ui.change_information(self.username, date, departure, destination)
                        self.query_result_login_ui.ui.show()
                    else:
                        self.query_result_ui.change_information(date, departure, destination)
                        self.query_result_ui.ui.show()
                else:
                    QMessageBox.information(self.query_ui.ui, '提示',
                                            '可选日期为：' + str([d[0].strftime("%Y-%m-%d") for d in result]))
        except Exception as e:
            err_print(self.query_ui.ui, e)

    def query_result_login_back(self):
        self.query_result_login_ui.ui.close()
        self.main_ui.ui.show()

    def logout(self):
        self.login_status = False
        self.query_result_login_ui.ui.close()
        self.main_ui.ui.show()

    def query_result_back(self):
        self.query_result_ui.ui.close()
        self.main_ui.ui.show()

    def query_result_to_login(self):
        self.query_result_ui.ui.close()
        self.login_ui.ui.show()

    def query_result_to_register(self):
        self.query_result_ui.ui.close()
        self.register_ui.ui.show()


def db_connect():
    """
    阿里云数据库连接

    :return: server, connect_obj, cursor
    """
    try:
        # 通过SSH连接云服务器
        server = SSHTunnelForwarder(
            ssh_address_or_host=('120.79.14.209', 22),  # 云服务器地址IP和端口port
            ssh_username='mysql_db',  # 云服务器登录账号
            ssh_password='mysql_db',  # 云服务器登录密码
            remote_bind_address=('localhost', 3306)  # 数据库服务地址ip,一般为localhost和端口port，一般为3306
        )
        # 云服务器开启
        server.start()
        # 云服务器上mysql数据库连接
        connect_obj = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                                      port=server.local_bind_port,
                                      user='stms',  # mysql的登录账号
                                      password='stms',  # mysql的登录密码
                                      db='ticket_management_system',  # mysql中要访问的数据库
                                      charset='utf8')  # 表的字符集
        # 创建游标
        cursor = connect_obj.cursor()
        return server, connect_obj, cursor
    except Exception as e:
        print(e)


def main():
    Server, Connect_obj, Cursor = db_connect()

    if Cursor:
        try:
            app = QApplication(sys.argv)
            window = Main(Connect_obj, Cursor)
            window.main_ui.ui.show()
            app.exec_()
        except Exception as e:
            print(e)

    # 断开连接
    Cursor.close()
    Connect_obj.close()
    Server.close()


def run_local():
    Connect = pymysql.connect(host='localhost', user='root', password='root', database='ticket-managerment-system',
                              port=3306)
    Cursor = Connect.cursor()

    try:
        app = QApplication(sys.argv)
        window = Main(Connect, Cursor)
        window.main_ui.ui.show()
        app.exec_()
    except Exception as e:
        print(e)

    Cursor.close()
    Connect.close()


if __name__ == '__main__':
    # run_local()
    main()
