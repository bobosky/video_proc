#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# __Author__: WangGuobao(guobao.v@gmail.com)
# __Date__: 2018/7/6 0006

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

"""
程序入口
"""

import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication
import src.control.main_controller as control
__version__ = "0.1.0"

if __name__ == '__main__':

    # 创建应用程序
    app = QApplication(sys.argv)
    app.setOrganizationName("aimao")
    app.setOrganizationDomain("aimao.co")
    app.setApplicationName("Proc_Video_Demo")

    # 设置QSS样式
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    # 初始化窗口（GUI程序具体实现类）
    window = control.Window()

    # # 无边框窗口样式
    # window.setWindowFlags(Qt.FramelessWindowHint)

    # 最大化窗口（此时视频页最大可达1200*880）
    window.showMaximized()

    # # 获取电脑屏幕大小
    # desktop = app.desktop().availableGeometry()  # (0,0,1920,1040)可获得的桌面（高度减了任务栏）
    # # screen=app.desktop().screenGeometry() #(0,0,1920,1080) 屏幕大小

    # # 显示窗口
    # window.show()

    # # 获取应用窗口大小
    # size = window.frameGeometry()  # 应用的整体窗口形状，window.geometry()为客户区形状
    # # 显示居中
    # window.move((desktop.width() - size.width()) / 2, (desktop.height() - size.height()) / 2)

    # 若关闭则退出
    sys.exit(app.exec_())
