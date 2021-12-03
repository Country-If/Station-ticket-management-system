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
        self.rank_chosen = ""
        self.location_chosen = ""

        # 设置按钮组(designer里找不到在哪里改按钮组名字)，添加对应按钮，连接信号与槽
        self.ui.rank_btn_group = QButtonGroup()
        self.ui.rank_btn_group.addButton(self.ui.first_rbtn)
        self.ui.rank_btn_group.addButton(self.ui.second_rbtn)
        self.ui.rank_btn_group.buttonClicked.connect(self.rank_choose)

        self.ui.location_btn_group = QButtonGroup()
        self.ui.location_btn_group.addButton(self.ui.a_rbtn)
        self.ui.location_btn_group.addButton(self.ui.b_rbtn)
        self.ui.location_btn_group.addButton(self.ui.c_rbtn)
        self.ui.location_btn_group.addButton(self.ui.e_rbtn)
        self.ui.location_btn_group.addButton(self.ui.f_rbtn)
        self.ui.location_btn_group.buttonClicked.connect(self.location_choose)

    def get_result(self, result):
        """
        获取数据库查询结果

        :param result: 数据库查询结果
        :return: None
        """
        self.result = result

    def rank_choose(self):
        """
        获取座位等级选择结果

        :return: None
        """
        self.rank_chosen = self.ui.rank_btn_group.checkedButton().text()

    def location_choose(self):
        """
        获取座位位置选择结果

        :return: None
        """
        self.location_chosen = self.ui.location_btn_group.checkedButton().text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = seat_choose_ui()
    window.ui.show()
    app.exec_()
