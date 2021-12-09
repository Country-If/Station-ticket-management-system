#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from PySide2.QtWidgets import QApplication, QMessageBox, \
    QTableWidgetItem, QPushButton, QButtonGroup, QInputDialog, \
    QLineEdit
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QDate, Qt
import sys
import pymysql
from sshtunnel import SSHTunnelForwarder
import random
import datetime
import time


def err_print(ui, err):
    """
    报错弹窗

    :param ui: 父窗口
    :param err: 错误内容
    :return: None
    """
    QMessageBox.critical(ui, '错误', str(err))


def InputDialog_getText(ui, title, label):
    """
    弹出输入对话框获取文本信息

    :param ui: 父窗口
    :param title: 标题
    :param label: 标签
    :return: (str)输入内容
    """
    input_text, okPressed = QInputDialog.getText(ui, title, label, QLineEdit.Normal)
    if okPressed:
        if input_text:
            return input_text
        else:
            err_print(ui, '输入为空')


def InputDialog_getInt(ui, title, label):
    """
    弹出输入对话框获取整数

    :param ui: 父窗口
    :param title: 标题
    :param label: 标签
    :return: int
    """
    input_int, okPressed = QInputDialog.getInt(ui, title, label, 1, minValue=1, maxValue=10000)
    if okPressed:
        return input_int


def get_date(ui, title):
    """
    获取输入的日期

    :param ui: 父窗口
    :param title: 标题
    :return: str
    """
    input_date = InputDialog_getText(ui, title, '请输入日期(yyyy-MM-dd)')
    if input_date:
        try:
            time.strptime(input_date, '%Y-%m-%d')
            return input_date
        except ValueError:
            err_print(ui, "输入格式有误")
            return
        except Exception as e:
            err_print(ui, e)
            return


def get_time(ui, title):
    """
    获取输入的时间

    :param ui: 父窗口
    :param title: 标题
    :return: str
    """
    input_time = InputDialog_getText(ui, title, '请输入时间(HH:mm)')
    if input_time:
        try:
            time.strptime(input_time, '%H:%M')
            return input_time
        except ValueError:
            err_print(ui, "输入格式有误")
            return
        except Exception as e:
            err_print(ui, e)
            return
