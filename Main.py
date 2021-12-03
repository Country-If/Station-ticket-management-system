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
from user_center import user_center_ui
from booking_query import booking_query_ui
from seat_choose import seat_choose_ui


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
        self.user_center_ui = user_center_ui()
        self.booking_query_ui = booking_query_ui()
        self.seat_choose_ui = seat_choose_ui()

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
        self.query_result_login_ui.ui.logout_btn.clicked.connect(self.query_result_login_logout)

        self.query_result_ui.ui.back_btn.clicked.connect(self.query_result_back)
        self.query_result_ui.ui.login_btn.clicked.connect(self.query_result_to_login)
        self.query_result_ui.ui.register_btn.clicked.connect(self.query_result_to_register)

        self.user_center_ui.ui.info_query_btn.clicked.connect(self.user_center_to_query)
        self.user_center_ui.ui.booking_query_btn.clicked.connect(self.user_center_to_booking_query)
        self.user_center_ui.ui.logout_btn.clicked.connect(self.user_center_logout)

        self.booking_query_ui.ui.back_btn.clicked.connect(self.booking_query_back)

        self.seat_choose_ui.ui.back_btn.clicked.connect(self.seat_choose_back)
        self.seat_choose_ui.ui.confirm_btn.clicked.connect(self.seat_choose_confirm)

    """
    主要的界面切换函数
    """

    # main ui
    def main_to_register(self):
        """
        主界面前往注册界面

        :return: None
        """
        self.main_ui.ui.close()
        self.register_ui.ui.show()

    def main_to_login(self):
        """
        主界面前往登录界面

        :return: None
        """
        self.main_ui.ui.close()
        self.login_ui.ui.show()

    def main_to_query(self):
        """
        主界面前往查询界面

        :return: None
        """
        self.main_ui.ui.close()
        self.query_ui.ui.show()

    # register ui
    def register_back(self):
        """
        注册界面返回

        :return: None
        """
        self.register_ui.ui.close()
        self.main_ui.ui.show()

    # login ui
    def login_back(self):
        """
        登录界面返回

        :return: None
        """
        self.login_ui.ui.close()
        self.main_ui.ui.show()

    # query ui
    def query_back(self):
        """
        查询界面返回

        :return: None
        """
        # 若已登录则切换到个人中心界面
        if self.login_status:
            self.query_ui.ui.close()
            self.user_center_ui.ui.show()
        else:
            self.query_ui.ui.close()
            self.main_ui.ui.show()

    # query result ui
    def query_result_back(self):
        """
        登录前查询结果界面返回

        :return: None
        """
        self.query_result_ui.clear_table()
        self.query_result_ui.ui.close()
        self.main_ui.ui.show()

    def query_result_to_register(self):
        """
        登录前查询结果界面前往注册

        :return: None
        """
        self.query_result_ui.clear_table()
        self.query_result_ui.ui.close()
        self.register_ui.ui.show()

    def query_result_to_login(self):
        """
        登录前查询结果界面前往登录

        :return: None
        """
        self.query_result_ui.clear_table()
        self.query_result_ui.ui.close()
        self.login_ui.ui.show()

    # query result login ui
    def query_result_login_back(self):
        """
        登录后查询结果界面返回

        :return: None
        """
        self.query_result_login_ui.clear_table()
        self.query_result_login_ui.ui.close()
        self.main_ui.ui.show()

    def query_result_login_logout(self):
        """
        登录后查询结果界面注销

        :return: None
        """
        self.login_status = False
        self.query_result_login_ui.clear_table()
        self.query_result_login_ui.ui.close()
        self.main_ui.ui.show()

    # user center ui
    def user_center_to_query(self):
        """
        个人中心界面前往查询

        :return: None
        """
        self.user_center_ui.ui.close()
        self.query_ui.ui.show()

    def user_center_to_booking_query(self):
        """
        个人中心界面前往订单查询界面

        :return: None
        """
        self.user_center_ui.ui.close()
        self.booking_query_ui.setUsername(self.username)
        self.booking_query_ui.ui.show()

    def user_center_logout(self):
        """
        个人中心界面注销

        :return: None
        """
        self.login_status = False
        self.user_center_ui.ui.close()
        self.main_ui.ui.show()

    # booking query ui
    def booking_query_back(self):
        """
        订单查询界面返回

        :return: None
        """
        self.booking_query_ui.ui.close()
        self.user_center_ui.ui.show()

    # seat choose ui
    def seat_choose_back(self):
        """
        座位选择界面返回

        :return: None
        """
        self.seat_choose_ui.ui.close()
        self.query_result_login_ui.ui.show()

    """
    功能处理函数
    """

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
                    self.user_center_ui.set_username(self.username)
                    self.user_center_ui.ui.show()
                else:
                    QMessageBox.critical(self.login_ui.ui, '登录失败', '用户名或密码错误')
            except Exception as e:
                err_print(self.login_ui.ui, e)

    def query(self):
        """
        查询按钮功能

        :return: None
        """
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
        """
        已知终点站查询始发站

        :param destination: 终点站
        :return: None
        """
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
        """
        已知始发站查询终点站

        :param departure: 始发站
        :return: None
        """
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
        """
        检查日期及切换界面

        :param departure: 始发站
        :param destination: 终点站
        :param date: 日期
        :return: None
        """
        # 查询始发站和终点站是否有日期信息
        sql = r"select date from train_information where departure='%s' and destination='%s';" \
              % (departure, destination)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if len(result) == 0:
                QMessageBox.critical(self.query_ui.ui, '错误', '查询不到信息，请重新输入')
            else:
                # 对输入的日期进行检查和提示
                if datetime.date(*map(int, date.split('/'))) in [d[0] for d in result]:
                    QMessageBox.information(self.query_ui.ui, '提示', '查询成功')
                    # 根据登录状态切换界面
                    self.query_ui.ui.close()
                    if self.login_status:
                        self.query_result_login_ui.change_information(self.username, date, departure, destination)
                        self.query_result_login_ui.ui.show()
                        self.table_load_data(self.query_result_login_ui, departure, destination, date)
                    else:
                        self.query_result_ui.change_information(date, departure, destination)
                        self.query_result_ui.ui.show()
                        self.table_load_data(self.query_result_ui, departure, destination, date)
                else:
                    QMessageBox.information(self.query_ui.ui, '提示',
                                            '可选日期为：' + str([d[0].strftime("%Y-%m-%d") for d in result]))
        except Exception as e:
            err_print(self.query_ui.ui, e)

    def table_load_data(self, obj, departure, destination, date):
        """
        表格中加载数据及按钮

        :param obj: 加载的界面对象
        :param departure: 始发站
        :param destination: 终点站
        :param date: 日期
        :return: None
        """
        # sql = r"SELECT `train_information`.`train_id`,seat_id,departure_time,arrival_time,`rank`,`price`,`is_used` " \
        #       r"FROM `train_information`,`seat_information` " \
        #       r"WHERE `train_information`.`train_id`=`seat_information`.`train_id` " \
        #       r"AND `departure`='%s' AND `destination`='%s' AND `date`='%s';" \
        #       % (departure, destination, date)

        # sql = r"select `train_id`,`departure_time`,`arrival_time`,`first_left`,`second_left` " \
        #       r"from `train_information`," \
        #       r"(select count( *) first_left from `seat_information` where `train_id` in " \
        #       r"(select `train_id` from `train_information` " \
        #       r"where `departure`='%s' and `destination`='%s' and `date`='%s') " \
        #       r"and `rank`='一等座' and `is_used`=0 group by `rank`) a," \
        #       r"(select count( *) second_left from `seat_information` where `train_id` in " \
        #       r"(select `train_id` from `train_information` " \
        #       r"where `departure`='%s' and `destination`='%s' and `date`='%s') " \
        #       r"and `rank`='二等座' and `is_used`=0 group by `rank`) b " \
        #       r"where `departure`='%s' and `destination`='%s' and `date`='%s'" \
        #       % (departure, destination, date, departure, destination, date, departure, destination, date)

        sql = r"SELECT a.train_id,a.departure_time,a.arrival_time,b.first_left,c.second_left " \
              r"FROM train_information a " \
              r"LEFT JOIN (SELECT train_id,count(seat_id) first_left FROM seat_information " \
              r"WHERE `rank`='一等座' AND is_used = 0 GROUP BY train_id ) b ON a.train_id=b.train_id  " \
              r"LEFT JOIN (SELECT train_id,count(seat_id) second_left FROM seat_information " \
              r"WHERE `rank`='二等座' AND is_used = 0 GROUP BY train_id ) c on a.train_id=c.train_id " \
              r"WHERE a.departure = '%s'  AND a.destination = '%s'  AND a.date = '%s';" \
              % (departure, destination, date)
        try:
            # 数据库查询数据
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if len(result) == 0:
                raise ValueError("查询不到数据")
            # 插入数据
            for row in range(len(result)):  # 逐行
                obj.ui.result_table.insertRow(row)  # 新增一行
                for col in range(len(result[0]) + 1):  # 逐列
                    if col == len(result[0]):  # 表格最后一列，添加按钮
                        obj.ui.result_table.setCellWidget(row, col, self.buttonForRow(result[row]))
                    else:
                        item = QTableWidgetItem(str(result[row][col]))
                        item.setFlags(Qt.ItemIsEnabled)  # 设置单元格为只读
                        item.setTextAlignment(Qt.AlignCenter)  # 设置文本内容居中
                        obj.ui.result_table.setItem(row, col, item)
        except Exception as e:
            obj.clear_table()
            err_print(obj.ui, e)

    def buttonForRow(self, result):
        """
        每行表格最后一列添加按钮

        :param result: 数据库查询结果
        :return: QPushButton
        """
        btn = QPushButton('订票')
        btn.clicked.connect(lambda: self.booking(result))
        return btn

    def booking(self, result):
        """
        订票，切换座位选择界面

        :param result: 数据库查询结果
        :return: None
        """
        if self.login_status:
            self.query_result_login_ui.ui.close()
            self.seat_choose_ui.get_result(result)
            self.seat_choose_ui.ui.show()
        else:
            QMessageBox.information(self.query_result_ui.ui, '提示', '登录后才可以订票')

    def seat_choose_confirm(self):
        # ('K7722', datetime.timedelta(seconds=72505), datetime.timedelta(seconds=79705), 160, 800)
        result = self.seat_choose_ui.result
        if self.seat_choose_ui.rank_chosen == "" or self.seat_choose_ui.location_chosen == "":
            err_print(self.seat_choose_ui.ui, '请勾选必需选项')
        else:
            if result[-1] + result[-2] == 0:    # 无票
                QMessageBox.critical(self.seat_choose_ui.ui, '订票失败', '该车次已无票')
            elif result[-2] == 0 and self.seat_choose_ui.rank_chosen == '一等座':  # 一等座无票
                choice = QMessageBox.question(self.seat_choose_ui.ui, '确认', '该车次一等座已无票，若仍需订票请点击Yes，若放弃订票请点击No')
                if choice == QMessageBox.Yes:
                    self.seat_choose_ui.ui.close()
                    self.query_result_login_ui.ui.show()
                    return
                elif choice == QMessageBox.No:
                    pass
            elif result[-1] == 0 and self.seat_choose_ui.rank_chosen == '二等座':  # 二等座无票
                choice = QMessageBox.question(self.seat_choose_ui.ui, '确认', '该车次二等座已无票，若仍需订票请点击Yes，若放弃订票请点击No')
                if choice == QMessageBox.Yes:
                    self.seat_choose_ui.ui.close()
                    self.query_result_login_ui.ui.show()
                    return
                elif choice == QMessageBox.No:
                    pass
            else:
                sql = r"select seat_id from seat_information where train_id='%s' and `rank`='%s' and is_used=0;" \
                      % (result[0], self.seat_choose_ui.rank_chosen)
                print(sql)
            self.query_result_login_ui.clear_table()    # 记得将query_result_login_ui的表格清空
            self.seat_choose_ui.ui.close()
            self.user_center_ui.ui.show()


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
            Window = Main(Connect_obj, Cursor)
            Window.main_ui.ui.show()
            app.exec_()
        except Exception as e:
            print(e)

    # 断开连接
    Cursor.close()
    Connect_obj.close()
    Server.close()


def run_local():
    Connect = pymysql.connect(host='localhost', user='root', password='root', database='ticket_management_system',
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
    run_local()
    # main()
