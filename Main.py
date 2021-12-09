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
from management import management_ui


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
        self.management_ui = management_ui()

        # 信号与槽连接
        self.main_ui.ui.register_btn.clicked.connect(self.main_to_register)
        self.main_ui.ui.login_btn.clicked.connect(self.main_to_login)
        self.main_ui.ui.query_btn.clicked.connect(self.main_to_query)
        self.main_ui.ui.manage_btn.clicked.connect(self.main_to_management)

        self.register_ui.ui.back_btn.clicked.connect(self.register_back)

        self.login_ui.ui.back_btn.clicked.connect(self.login_back)
        self.login_ui.ui.password_label.returnPressed.connect(self.login)
        self.login_ui.ui.login_btn.clicked.connect(self.login)

        self.query_ui.ui.back_btn.clicked.connect(self.query_back)
        self.query_ui.ui.query_btn.clicked.connect(self.query)
        self.query_ui.ui.departure_label.returnPressed.connect(self.query)
        self.query_ui.ui.destination_label.returnPressed.connect(self.query)

        self.query_result_login_ui.ui.back_btn.clicked.connect(self.query_result_login_back)
        self.query_result_login_ui.ui.logout_btn.clicked.connect(self.query_result_login_logout)

        self.query_result_ui.ui.back_btn.clicked.connect(self.query_result_back)
        self.query_result_ui.ui.login_btn.clicked.connect(self.query_result_to_login)
        self.query_result_ui.ui.register_btn.clicked.connect(self.query_result_to_register)

        self.user_center_ui.ui.info_query_btn.clicked.connect(self.user_center_to_query)
        self.user_center_ui.ui.booking_query_btn.clicked.connect(self.user_center_to_booking_query)
        self.user_center_ui.ui.logout_btn.clicked.connect(self.user_center_logout)

        self.booking_query_ui.ui.back_btn.clicked.connect(self.booking_query_back)
        self.booking_query_ui.ui.logout_btn.clicked.connect(self.booking_query_logout)

        self.seat_choose_ui.ui.back_btn.clicked.connect(self.seat_choose_back)
        self.seat_choose_ui.ui.confirm_btn.clicked.connect(self.seat_choose_confirm)

        self.management_ui.ui.back_btn.clicked.connect(self.management_back)
        self.management_ui.ui.update_btn.clicked.connect(self.management_to_update)
        self.management_ui.ui.insert_btn.clicked.connect(self.management_to_insert)
        self.management_ui.ui.delete_btn.clicked.connect(self.management_to_delete)

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

    def main_to_management(self):
        """
        主界面前往管理界面

        :return: None
        """
        self.main_ui.ui.close()
        self.management_ui.ui.show()

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
        self.user_center_ui.ui.show()

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
        self.booking_query_table_load_data()

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
        self.booking_query_ui.clear_table()
        self.booking_query_ui.ui.close()
        self.user_center_ui.ui.show()

    def booking_query_logout(self):
        """
        订单查询结果界面注销

        :return: None
        """
        self.login_status = False
        self.booking_query_ui.clear_table()
        self.booking_query_ui.ui.close()
        self.main_ui.ui.show()

    # seat choose ui
    def seat_choose_back(self):
        """
        座位选择界面返回

        :return: None
        """
        self.seat_choose_ui.ui.close()
        self.query_result_login_ui.ui.show()

    # management ui
    def management_back(self):
        """
        管理界面返回

        :return: None
        """
        self.management_ui.ui.close()
        self.main_ui.ui.show()

    """
    主要功能处理函数
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
            sql = r"select * from user_information where user_name='%s' and password='%s';" \
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
                        self.query_result_table_load_data(self.query_result_login_ui, departure, destination, date)
                    else:
                        self.query_result_ui.change_information(date, departure, destination)
                        self.query_result_ui.ui.show()
                        self.query_result_table_load_data(self.query_result_ui, departure, destination, date)
                else:
                    QMessageBox.information(self.query_ui.ui, '提示',
                                            '可选日期为：' + str([d[0].strftime("%Y-%m-%d") for d in result]))
        except Exception as e:
            err_print(self.query_ui.ui, e)

    def query_result_table_load_data(self, obj, departure, destination, date):
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
        #       r"where `departure`='%s' and `destination`='%s' and `date`='%s';" \
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
            else:
                # 插入数据
                for row in range(len(result)):  # 逐行
                    obj.ui.result_table.insertRow(row)  # 新增一行
                    for col in range(len(result[0]) + 1):  # 逐列
                        if col == len(result[0]):  # 表格最后一列，添加按钮
                            obj.ui.result_table.setCellWidget(row, col,
                                                              self.query_result_buttonForRow(result[row], date))
                        else:
                            if result[row][col] is None:
                                item = QTableWidgetItem(str(0))
                            else:
                                item = QTableWidgetItem(str(result[row][col]))
                            item.setFlags(Qt.ItemIsEnabled)  # 设置单元格为只读
                            item.setTextAlignment(Qt.AlignCenter)  # 设置文本内容居中
                            obj.ui.result_table.setItem(row, col, item)
        except Exception as e:
            obj.clear_table()
            err_print(obj.ui, e)

    def booking(self, result, date):
        """
        订票，切换座位选择界面

        :param result: 数据库查询结果
        :param date: 日期
        :return: None
        """
        if self.login_status:
            self.query_result_login_ui.ui.close()
            self.seat_choose_ui.get_information(result, date)
            self.seat_choose_ui.ui.show()
        else:
            QMessageBox.information(self.query_result_ui.ui, '提示', '登录后才可以订票')

    def seat_choose_confirm(self):
        """
        座位选择界面的确定按钮处理函数

        :return: None
        """
        flag = False  # 订票成功标志
        result = self.seat_choose_ui.result
        date = self.seat_choose_ui.date
        # 判断按钮勾选是否完整
        if self.seat_choose_ui.rank_chosen == "" or self.seat_choose_ui.location_chosen == "":  # 勾选不完整
            err_print(self.seat_choose_ui.ui, '请勾选必需选项')
        else:
            # 判断座位的票数是否符合需求
            if result[-1] is None and result[-2] is None:  # 无票
                QMessageBox.critical(self.seat_choose_ui.ui, '订票失败', '该车次已无票')
            elif result[-2] is None and self.seat_choose_ui.rank_chosen == '一等座':  # 一等座无票
                choice = QMessageBox.question(self.seat_choose_ui.ui, '确认', '该车次一等座已无票，若仍需订票请点击Yes，若放弃订票请点击No')
                if choice == QMessageBox.Yes:
                    self.seat_choose_ui.ui.close()
                    self.query_result_login_ui.ui.show()
                    return
                elif choice == QMessageBox.No:
                    pass
            elif result[-1] is None and self.seat_choose_ui.rank_chosen == '二等座':  # 二等座无票
                choice = QMessageBox.question(self.seat_choose_ui.ui, '确认', '该车次二等座已无票，若仍需订票请点击Yes，若放弃订票请点击No')
                if choice == QMessageBox.Yes:
                    self.seat_choose_ui.ui.close()
                    self.query_result_login_ui.ui.show()
                    return
                elif choice == QMessageBox.No:
                    pass
            else:  # 余票满足要求
                sql = r"select seat_id from seat_information where train_id='%s' and `rank`='%s' and is_used=0;" \
                      % (result[0], self.seat_choose_ui.rank_chosen)
                try:
                    self.cursor.execute(sql)
                    seat_id_tuple = self.cursor.fetchall()
                    for seat_id in seat_id_tuple:
                        # 用户选取的座位位置有票
                        if self.seat_choose_ui.location_chosen in seat_id[0]:
                            sql_query = r"select `rank`,`price` from seat_information " \
                                        r"where `train_id`='%s' and `seat_id`='%s';" \
                                        % (result[0], seat_id[0])
                            try:
                                self.cursor.execute(sql_query)
                                rank_price = self.cursor.fetchall()  # 获取座位等级和价格
                                sql_update = r"update seat_information set `is_used`=1 " \
                                             r"where `train_id`='%s' and `seat_id`='%s';" \
                                             % (result[0], seat_id[0])
                                sql_insert = r"insert into booking_information " \
                                             r"(`user_name`, `train_id`, `seat_id`, " \
                                             r"`date`, `departure_time`, `rank`, `price`) " \
                                             r"values ('%s','%s','%s','%s','%s','%s','%s');" \
                                             % (self.username, result[0], seat_id[0], date, result[1], rank_price[0][0],
                                                rank_price[0][1])
                                try:
                                    self.cursor.execute(sql_update)  # 修改对应座位的占用标识
                                    self.connect_obj.commit()
                                    self.cursor.execute(sql_insert)  # 插入购票表
                                    self.connect_obj.commit()
                                    flag = True
                                    QMessageBox.information(self.seat_choose_ui.ui, '提示', '订票成功，座位为：' + str(seat_id[0]))
                                    break
                                except Exception as e:
                                    self.connect_obj.rollback()
                                    err_print(self.seat_choose_ui.ui, e)
                            except Exception as e:
                                err_print(self.seat_choose_ui.ui, e)
                    # 用户选取的座位位置无票
                    if not flag:
                        seat_id = seat_id_tuple[0]  # 取tuple中第一个位置
                        sql_query = r"select `rank`,`price` from seat_information " \
                                    r"where `train_id`='%s' and `seat_id`='%s';" \
                                    % (result[0], seat_id[0])
                        try:
                            self.cursor.execute(sql_query)
                            rank_price = self.cursor.fetchall()  # 获取座位等级和价格
                            sql_update = r"update seat_information set `is_used`=1 " \
                                         r"where `train_id`='%s' and `seat_id`='%s';" \
                                         % (result[0], seat_id[0])
                            sql_insert = r"insert into booking_information " \
                                         r"(`user_name`,`train_id`,`seat_id`,`date`,`departure_time`,`rank`,`price`) " \
                                         r"values ('%s','%s','%s','%s','%s','%s','%s');" \
                                         % (self.username, result[0], seat_id[0], date, result[1], rank_price[0][0],
                                            rank_price[0][1])
                            try:
                                self.cursor.execute(sql_update)  # 修改对应座位的占用标识
                                self.connect_obj.commit()
                                self.cursor.execute(sql_insert)  # 插入购票表
                                self.connect_obj.commit()
                                QMessageBox.information(self.seat_choose_ui.ui, '提示',
                                                        '所选位置无票，系统已为你选取座位：' + str(seat_id[0]))
                            except Exception as e:
                                self.connect_obj.rollback()
                                err_print(self.seat_choose_ui.ui, e)
                        except Exception as e:
                            err_print(self.seat_choose_ui.ui, e)
                except Exception as e:
                    err_print(self.seat_choose_ui.ui, e)
            self.query_result_login_ui.clear_table()  # 记得将query_result_login_ui的表格清空
            self.seat_choose_ui.ui.close()
            self.user_center_ui.ui.show()

    def booking_query_table_load_data(self):
        """
        订单查询界面加载表格数据

        :return: None
        """
        sql = r"select booking_id,train_id,seat_id,date,departure_time,`rank`,price from booking_information " \
              r"where user_name='%s' and is_deleted=0;" % self.username
        try:
            # 数据库查询数据
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            # 插入数据
            for row in range(len(result)):  # 逐行
                self.booking_query_ui.ui.result_table.insertRow(row)  # 新增一行
                for col in range(len(result[0]) + 1):  # 逐列
                    if col == len(result[0]):  # 表格最后一列，添加按钮
                        self.booking_query_ui.ui.result_table.setCellWidget(row, col, self.booking_query_buttonForRow(
                            result[row]))
                    else:
                        item = QTableWidgetItem(str(result[row][col]))
                        item.setFlags(Qt.ItemIsEnabled)  # 设置单元格为只读
                        item.setTextAlignment(Qt.AlignCenter)  # 设置文本内容居中
                        self.booking_query_ui.ui.result_table.setItem(row, col, item)
        except Exception as e:
            err_print(self.booking_query_ui.ui, e)

    def refund(self, result):
        """
        处理退票

        :param result: 数据库查询结果
        :return: None
        """
        booking_id = result[0]
        train_id = result[1]
        seat_id = result[2]
        sql_update_booking = r"update booking_information set `is_deleted`=1 where `booking_id`='%s';" % booking_id
        sql_update_seat = r"update seat_information set `is_used`=0 where `train_id`='%s' and `seat_id`='%s';" \
                          % (train_id, seat_id)
        try:
            self.cursor.execute(sql_update_booking)
            self.connect_obj.commit()
            self.cursor.execute(sql_update_seat)
            self.connect_obj.commit()
            QMessageBox.information(self.booking_query_ui.ui, '提示', '退票成功')
            # 重新加载，更新数据
            self.booking_query_ui.clear_table()
            self.booking_query_table_load_data()
        except Exception as e:
            self.connect_obj.rollback()
            err_print(self.booking_query_ui.ui, e)

    def management_to_update(self):
        """
        获取修改信息并修改

        :return: None
        """
        input_train_id = InputDialog_getText(self.management_ui.ui, '修改', '请输入车次')
        if input_train_id:
            sql_query_train = r"select train_id from train_information where `train_id`='%s';" % input_train_id
            try:
                self.cursor.execute(sql_query_train)
                result = self.cursor.fetchall()
                if len(result) == 0:
                    QMessageBox.critical(self.management_ui.ui, '查询失败', '查询不到车次信息')
                else:
                    update_items = ('始发站', '终点站', '日期', '发车时间', '到达时间', '一等座票价', '二等座票价')
                    update_item, okPressed = QInputDialog.getItem(self.management_ui.ui, '修改', '选择修改内容', update_items,
                                                                  0, False)
                    if okPressed:
                        if update_item == update_items[0]:
                            updated_departure = InputDialog_getText(self.management_ui.ui, '修改', '请输入修改后的始发站')
                            if updated_departure:
                                sql_update = r"update train_information set `departure`='%s' where `train_id`='%s';" \
                                             % (updated_departure, input_train_id)
                                flag = self.sql_update_func(self.management_ui.ui, sql_update)
                                if flag:
                                    QMessageBox.information(self.management_ui.ui, '提示', '修改成功')
                        elif update_item == update_items[1]:
                            updated_destination = InputDialog_getText(self.management_ui.ui, '修改', '请输入修改后的终点站')
                            if updated_destination:
                                sql_update = r"update train_information set `destination`='%s' where `train_id`='%s';" \
                                             % (updated_destination, input_train_id)
                                flag = self.sql_update_func(self.management_ui.ui, sql_update)
                                if flag:
                                    QMessageBox.information(self.management_ui.ui, '提示', '修改成功')
                        elif update_item == update_items[2]:
                            updated_date = get_date(self.management_ui.ui, '修改')
                            if updated_date:
                                sql_update = r"update train_information set `date`='%s' where `train_id`='%s';" \
                                             % (updated_date, input_train_id)
                                flag = self.sql_update_func(self.management_ui.ui, sql_update)
                                if flag:
                                    QMessageBox.information(self.management_ui.ui, '提示', '修改成功')
                        elif update_item == update_items[3]:
                            updated_departure_time = get_time(self.management_ui.ui, '修改')
                            if updated_departure_time:
                                sql_update = r"update train_information set `departure_time`='%s' " \
                                             r"where `train_id`='%s';" \
                                             % (updated_departure_time, input_train_id)
                                flag = self.sql_update_func(self.management_ui.ui, sql_update)
                                if flag:
                                    QMessageBox.information(self.management_ui.ui, '提示', '修改成功')
                        elif update_item == update_items[4]:
                            updated_arrival_time = get_time(self.management_ui.ui, '修改')
                            if updated_arrival_time:
                                sql_update = r"update train_information set `arrival_time`='%s' " \
                                             r"where `train_id`='%s';" \
                                             % (updated_arrival_time, input_train_id)
                                flag = self.sql_update_func(self.management_ui.ui, sql_update)
                                if flag:
                                    QMessageBox.information(self.management_ui.ui, '提示', '修改成功')
                        elif update_item == update_items[5]:
                            price = InputDialog_getInt(self.management_ui.ui, '修改', '请输入修改后的一等座票价')
                            if price:
                                sql_update = r"update seat_information set `price`='%s' " \
                                             r"where `train_id`='%s' and `rank`='一等座';" \
                                             % (price, input_train_id)
                                flag = self.sql_update_func(self.management_ui.ui, sql_update)
                                if flag:
                                    QMessageBox.information(self.management_ui.ui, '提示', '修改成功')
                        else:
                            price = InputDialog_getInt(self.management_ui.ui, '修改', '请输入修改后的二等座票价')
                            if price:
                                sql_update = r"update seat_information set `price`='%s' " \
                                             r"where `train_id`='%s' and `rank`='二等座';" \
                                             % (price, input_train_id)
                                flag = self.sql_update_func(self.management_ui.ui, sql_update)
                                if flag:
                                    QMessageBox.information(self.management_ui.ui, '提示', '修改成功')
            except Exception as e:
                err_print(self.management_ui.ui, e)

    def management_to_insert(self):
        """
        获取插入信息并插入

        :return: None
        """
        train_id = self.generate_train_id()
        departure = InputDialog_getText(self.management_ui.ui, '插入', '请输入始发站')
        if departure:
            destination = InputDialog_getText(self.management_ui.ui, '插入', '请输入终点站')
            if destination:
                if destination == departure:
                    err_print(self.management_ui.ui, '始发站和终点站重复')
                else:
                    date = get_date(self.management_ui.ui, '插入')
                    if date:
                        # 对输入的日期判断其合理性
                        now = datetime.datetime.now()
                        if (now - datetime.datetime.strptime(date, '%Y-%m-%d')) > datetime.timedelta(days=0):
                            err_print(self.management_ui.ui, '输入的日期有误，日期至少应延后一天')
                        else:
                            departure_time = get_time(self.management_ui.ui, '发车时间')
                            if departure_time:
                                arrival_time = get_time(self.management_ui.ui, '到达时间')
                                if arrival_time:
                                    first_price = InputDialog_getInt(self.management_ui.ui, '插入', '请输入一等座票价')
                                    if first_price:
                                        second_price = InputDialog_getInt(self.management_ui.ui, '插入', '请输入二等座票价')
                                        if second_price:
                                            # 对输入的价格判断其合理性
                                            if first_price <= second_price:
                                                err_print(self.management_ui.ui, '价格设置不合理，一等座票价应高于二等座票价')
                                            else:
                                                flag = self.insert_train_seat(train_id, departure, destination,
                                                                              date, departure_time, arrival_time,
                                                                              first_price, second_price)
                                                if flag:
                                                    QMessageBox.information(self.management_ui.ui, '添加成功',
                                                                            '添加的车次为：' + train_id)

    def management_to_delete(self):
        """
        获取删除信息并删除

        :return: None
        """
        train_id = InputDialog_getText(self.management_ui.ui, '删除', '请输入要删除的车次')
        sql_query_train = r"select * from train_information where train_id='%s';" % train_id
        try:
            # 查询有无对应车次的信息
            self.cursor.execute(sql_query_train)
            result = self.cursor.fetchall()
            if len(result) == 0:
                err_print(self.management_ui.ui, '查询不到该车次信息')
            else:
                # 确认删除提示
                choice = QMessageBox.question(self.management_ui.ui, '确认', '确认执行删除操作？此操作不可撤销！')
                if choice == QMessageBox.Yes:
                    # 执行删除操作
                    sql_delete = r"delete from train_information where train_id='%s';" % train_id
                    try:
                        self.cursor.execute(sql_delete)
                        self.connect_obj.commit()
                        QMessageBox.information(self.management_ui.ui, '成功', '该车次已成功删除')
                    except Exception as e:
                        err_print(self.management_ui.ui, e)
                        self.connect_obj.rollback()
                elif choice == QMessageBox.No:
                    pass
        except Exception as e:
            err_print(self.management_ui.ui, e)

    """
    辅助处理函数
    """

    def query_result_buttonForRow(self, result, date):
        """
        每行表格最后一列添加按钮

        :param result: 数据库查询结果
        :param date: 日期
        :return: QPushButton
        """
        btn = QPushButton('订票')
        btn.clicked.connect(lambda: self.booking(result, date))
        return btn

    def booking_query_buttonForRow(self, result):
        """
        每行表格最后一列添加按钮

        :param result: 数据库查询结果
        :return: QPushButton
        """
        btn = QPushButton('退票')
        btn.clicked.connect(lambda: self.refund(result))
        return btn

    def sql_update_func(self, ui, sql_update):
        """
        数据库更新操作

        :param ui: 父窗口
        :param sql_update: SQL更新语句
        :return: bool
        """
        try:
            self.cursor.execute(sql_update)
            self.connect_obj.commit()
            return True
        except Exception as e:
            err_print(ui, e)
            self.connect_obj.rollback()
            return False

    def generate_train_id(self):
        """
        随机生成车次

        :return: (str)车次
        """
        while True:
            train_id = random.choice(['G', 'K', 'D', 'L']) + str(random.randint(1000, 9999))
            sql = r"select * from train_information where `train_id`='%s';" % train_id
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                if len(result) == 0:
                    return train_id
            except Exception as e:
                err_print(self.management_ui.ui, e)

    def insert_train_seat(self, train_id, departure, destination, date, departure_time, arrival_time,
                          first_price, second_price):
        """
        管理界面插入数据实现函数

        :param train_id: 车次
        :param departure: 始发站
        :param destination: 终点站
        :param date: 日期
        :param departure_time: 发车时间
        :param arrival_time: 到达时间
        :param first_price: 一等座票价
        :param second_price: 二等座票价
        :return: bool
        """
        # 插入车次表
        sql_insert_train = r"insert into train_information (train_id, departure, destination, " \
                           r"date, departure_time, arrival_time) " \
                           r"values ('%s', '%s', '%s', '%s', '%s', '%s');" \
                           % (train_id, departure, destination, date, departure_time, arrival_time)
        try:
            self.cursor.execute(sql_insert_train)
            self.connect_obj.commit()
        except Exception as e:
            err_print(self.management_ui.ui, e)
            self.connect_obj.rollback()
            return False

        row_num = 3  # 车数
        col_num = 4  # 座位排数
        seat_id_list = []
        rank_list = []
        price_list = []
        # 造数据
        for row in range(1, row_num + 1):
            for col in range(1, col_num + 1):
                if row == 1:
                    for t in ['A', 'B']:
                        seat_id_list.append('0' + str(row) + '车' + '0' + str(col) + t)
                        rank_list.append('一等座')
                        price_list.append(first_price)
                else:
                    for t in ['A', 'B', 'C', 'E', 'F']:
                        seat_id_list.append('0' + str(row) + '车' + '0' + str(col) + t)
                        rank_list.append('二等座')
                        price_list.append(second_price)
        # 插入座位表
        for i in range(len(seat_id_list)):
            sql_insert_seat = r"insert into seat_information (train_id, seat_id, `rank`, price, is_used) " \
                              r"values ('%s', '%s', '%s', '%s', '%s');" \
                              % (train_id, seat_id_list[i], rank_list[i], price_list[i], 0)
            try:
                self.cursor.execute(sql_insert_seat)
                self.connect_obj.commit()
            except Exception as e:
                err_print(self.management_ui.ui, e)
                self.connect_obj.rollback()
                return False
        return True


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
    """
    主程序入口

    :return: None
    """
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
    """
    本地测试

    :return: None
    """
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
    # run_local()
    main()
