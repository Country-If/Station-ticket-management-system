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
        return input_text


def InputDialog_getPrice(ui, title, label):
    """
    弹出输入对话框获取票价

    :param ui: 父窗口
    :param title: 标题
    :param label: 标签
    :return: (int)票价
    """
    input_int, okPressed = QInputDialog.getInt(ui, title, label, 100, minValue=10, maxValue=10000)
    if okPressed:
        return input_int
