#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QDate
import sys
import pymysql
from sshtunnel import SSHTunnelForwarder
import datetime


def err_print(ui, err):
    QMessageBox.critical(ui, '错误', str(err))
