# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1692, 760)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/res/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1692, 23))
        self.menubar.setObjectName("menubar")
        self.menu_menu = QtWidgets.QMenu(self.menubar)
        self.menu_menu.setObjectName("menu_menu")
        self.menu_view = QtWidgets.QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_frame = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_frame.setObjectName("dockWidget_frame")
        self.dockWidgetContents_frame = QtWidgets.QWidget()
        self.dockWidgetContents_frame.setObjectName("dockWidgetContents_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents_frame)
        self.scrollArea.setMinimumSize(QtCore.QSize(980, 550))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContents_frame = QtWidgets.QWidget()
        self.scrollAreaContents_frame.setGeometry(QtCore.QRect(0, 0, 976, 637))
        self.scrollAreaContents_frame.setMinimumSize(QtCore.QSize(960, 540))
        self.scrollAreaContents_frame.setObjectName("scrollAreaContents_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaContents_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_showFrame = QtWidgets.QLabel(self.scrollAreaContents_frame)
        self.label_showFrame.setEnabled(True)
        self.label_showFrame.setMinimumSize(QtCore.QSize(960, 540))
        self.label_showFrame.setObjectName("label_showFrame")
        self.verticalLayout_3.addWidget(self.label_showFrame)
        self.scrollArea.setWidget(self.scrollAreaContents_frame)
        self.verticalLayout.addWidget(self.scrollArea)
        self.dockWidget_frame.setWidget(self.dockWidgetContents_frame)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_frame)
        self.dockWidget_settings = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_settings.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_settings.setObjectName("dockWidget_settings")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(650, 550))
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaContents_settings = QtWidgets.QWidget()
        self.scrollAreaContents_settings.setGeometry(QtCore.QRect(0, 0, 646, 637))
        self.scrollAreaContents_settings.setMinimumSize(QtCore.QSize(646, 540))
        self.scrollAreaContents_settings.setObjectName("scrollAreaContents_settings")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaContents_settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaContents_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_vfile = QtWidgets.QWidget()
        self.tab_vfile.setObjectName("tab_vfile")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_vfile)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pBtn_getFile = QtWidgets.QPushButton(self.tab_vfile)
        self.pBtn_getFile.setObjectName("pBtn_getFile")
        self.gridLayout_2.addWidget(self.pBtn_getFile, 0, 3, 1, 1)
        self.lineEdit_videoFile = QtWidgets.QLineEdit(self.tab_vfile)
        self.lineEdit_videoFile.setDragEnabled(False)
        self.lineEdit_videoFile.setObjectName("lineEdit_videoFile")
        self.gridLayout_2.addWidget(self.lineEdit_videoFile, 0, 2, 1, 1)
        self.label_videoFile = QtWidgets.QLabel(self.tab_vfile)
        self.label_videoFile.setObjectName("label_videoFile")
        self.gridLayout_2.addWidget(self.label_videoFile, 0, 1, 1, 1)
        self.label_saveDir = QtWidgets.QLabel(self.tab_vfile)
        self.label_saveDir.setObjectName("label_saveDir")
        self.gridLayout_2.addWidget(self.label_saveDir, 1, 1, 1, 1)
        self.lineEdit_saveDir = QtWidgets.QLineEdit(self.tab_vfile)
        self.lineEdit_saveDir.setObjectName("lineEdit_saveDir")
        self.gridLayout_2.addWidget(self.lineEdit_saveDir, 1, 2, 1, 1)
        self.pBtn_getDir = QtWidgets.QPushButton(self.tab_vfile)
        self.pBtn_getDir.setObjectName("pBtn_getDir")
        self.gridLayout_2.addWidget(self.pBtn_getDir, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab_vfile, "")
        self.tab_cam = QtWidgets.QWidget()
        self.tab_cam.setObjectName("tab_cam")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_cam)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_cam_num = QtWidgets.QLabel(self.tab_cam)
        self.label_cam_num.setObjectName("label_cam_num")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_cam_num)
        self.sBox_cam_num = QtWidgets.QSpinBox(self.tab_cam)
        self.sBox_cam_num.setObjectName("sBox_cam_num")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sBox_cam_num)
        self.tabWidget.addTab(self.tab_cam, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.line = QtWidgets.QFrame(self.scrollAreaContents_settings)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.widget_set = QtWidgets.QWidget(self.scrollAreaContents_settings)
        self.widget_set.setObjectName("widget_set")
        self.formLayout = QtWidgets.QFormLayout(self.widget_set)
        self.formLayout.setObjectName("formLayout")
        self.label_scene = QtWidgets.QLabel(self.widget_set)
        self.label_scene.setObjectName("label_scene")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_scene)
        self.cBox_scene = QtWidgets.QComboBox(self.widget_set)
        self.cBox_scene.setEnabled(True)
        self.cBox_scene.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cBox_scene.setObjectName("cBox_scene")
        self.cBox_scene.addItem("")
        self.cBox_scene.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cBox_scene)
        self.label_history = QtWidgets.QLabel(self.widget_set)
        self.label_history.setObjectName("label_history")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_history)
        self.sBox_history = QtWidgets.QSpinBox(self.widget_set)
        self.sBox_history.setMaximum(100000)
        self.sBox_history.setObjectName("sBox_history")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sBox_history)
        self.label_threshold = QtWidgets.QLabel(self.widget_set)
        self.label_threshold.setObjectName("label_threshold")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_threshold)
        self.sBox_threshold = QtWidgets.QSpinBox(self.widget_set)
        self.sBox_threshold.setMaximum(1000)
        self.sBox_threshold.setObjectName("sBox_threshold")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sBox_threshold)
        self.label_area = QtWidgets.QLabel(self.widget_set)
        self.label_area.setObjectName("label_area")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_area)
        self.sBox_area = QtWidgets.QSpinBox(self.widget_set)
        self.sBox_area.setMaximum(1000000)
        self.sBox_area.setSingleStep(100)
        self.sBox_area.setObjectName("sBox_area")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sBox_area)
        self.label_ratio = QtWidgets.QLabel(self.widget_set)
        self.label_ratio.setObjectName("label_ratio")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_ratio)
        self.dsBox_ratio = QtWidgets.QDoubleSpinBox(self.widget_set)
        self.dsBox_ratio.setMaximum(1.0)
        self.dsBox_ratio.setSingleStep(0.01)
        self.dsBox_ratio.setObjectName("dsBox_ratio")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.dsBox_ratio)
        self.label_interruptframes = QtWidgets.QLabel(self.widget_set)
        self.label_interruptframes.setObjectName("label_interruptframes")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_interruptframes)
        self.sBox_undetframes = QtWidgets.QSpinBox(self.widget_set)
        self.sBox_undetframes.setMaximum(10000)
        self.sBox_undetframes.setObjectName("sBox_undetframes")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sBox_undetframes)
        self.label_blursize = QtWidgets.QLabel(self.widget_set)
        self.label_blursize.setObjectName("label_blursize")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_blursize)
        self.sBox_blursize = QtWidgets.QSpinBox(self.widget_set)
        self.sBox_blursize.setObjectName("sBox_blursize")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.sBox_blursize)
        self.label_autoback = QtWidgets.QLabel(self.widget_set)
        self.label_autoback.setObjectName("label_autoback")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_autoback)
        self.cBox_autoback = QtWidgets.QCheckBox(self.widget_set)
        self.cBox_autoback.setText("")
        self.cBox_autoback.setObjectName("cBox_autoback")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.cBox_autoback)
        self.label_shadow = QtWidgets.QLabel(self.widget_set)
        self.label_shadow.setObjectName("label_shadow")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_shadow)
        self.cBox_shadow = QtWidgets.QCheckBox(self.widget_set)
        self.cBox_shadow.setText("")
        self.cBox_shadow.setObjectName("cBox_shadow")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.cBox_shadow)
        self.label_shadowvar = QtWidgets.QLabel(self.widget_set)
        self.label_shadowvar.setObjectName("label_shadowvar")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_shadowvar)
        self.dsBox_shadowvar = QtWidgets.QDoubleSpinBox(self.widget_set)
        self.dsBox_shadowvar.setMaximum(1.0)
        self.dsBox_shadowvar.setSingleStep(0.01)
        self.dsBox_shadowvar.setObjectName("dsBox_shadowvar")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.dsBox_shadowvar)
        self.label_foreproc = QtWidgets.QLabel(self.widget_set)
        self.label_foreproc.setObjectName("label_foreproc")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_foreproc)
        self.cBox_foreproc = QtWidgets.QCheckBox(self.widget_set)
        self.cBox_foreproc.setText("")
        self.cBox_foreproc.setObjectName("cBox_foreproc")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.cBox_foreproc)
        self.label_erodeshape = QtWidgets.QLabel(self.widget_set)
        self.label_erodeshape.setObjectName("label_erodeshape")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_erodeshape)
        self.cBox_erodeshape = QtWidgets.QComboBox(self.widget_set)
        self.cBox_erodeshape.setObjectName("cBox_erodeshape")
        self.cBox_erodeshape.addItem("")
        self.cBox_erodeshape.addItem("")
        self.cBox_erodeshape.addItem("")
        self.cBox_erodeshape.addItem("")
        self.cBox_erodeshape.addItem("")
        self.cBox_erodeshape.addItem("")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.cBox_erodeshape)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(17, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_set)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaContents_settings)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.widget_back = QtWidgets.QWidget(self.scrollAreaContents_settings)
        self.widget_back.setObjectName("widget_back")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_back)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pBtn_getBackground = QtWidgets.QPushButton(self.widget_back)
        self.pBtn_getBackground.setObjectName("pBtn_getBackground")
        self.verticalLayout_5.addWidget(self.pBtn_getBackground)
        self.pBtn_showBackground = QtWidgets.QPushButton(self.widget_back)
        self.pBtn_showBackground.setObjectName("pBtn_showBackground")
        self.verticalLayout_5.addWidget(self.pBtn_showBackground)
        self.verticalLayout_2.addWidget(self.widget_back)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaContents_settings)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaContents_settings)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.scrollArea_2.setWidget(self.scrollAreaContents_settings)
        self.verticalLayout1.addWidget(self.scrollArea_2)
        self.dockWidget_settings.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_settings)
        self.action_run = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/res/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_run.setIcon(icon1)
        self.action_run.setObjectName("action_run")
        self.action_stop = QtWidgets.QAction(MainWindow)
        self.action_stop.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/picture/res/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_stop.setIcon(icon2)
        self.action_stop.setObjectName("action_stop")
        self.action_pause = QtWidgets.QAction(MainWindow)
        self.action_pause.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/picture/res/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_pause.setIcon(icon3)
        self.action_pause.setObjectName("action_pause")
        self.action_view_restore = QtWidgets.QAction(MainWindow)
        self.action_view_restore.setObjectName("action_view_restore")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu_menu.addAction(self.action_run)
        self.menu_menu.addAction(self.action_stop)
        self.menu_menu.addAction(self.action_pause)
        self.menu_view.addAction(self.action_view_restore)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_menu.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.toolBar.addAction(self.action_run)
        self.toolBar.addAction(self.action_pause)
        self.toolBar.addAction(self.action_stop)
        self.label_videoFile.setBuddy(self.lineEdit_videoFile)
        self.label_saveDir.setBuddy(self.lineEdit_saveDir)
        self.label_scene.setBuddy(self.cBox_scene)
        self.label_history.setBuddy(self.sBox_history)
        self.label_threshold.setBuddy(self.sBox_threshold)
        self.label_area.setBuddy(self.sBox_area)
        self.label_ratio.setBuddy(self.dsBox_ratio)
        self.label_interruptframes.setBuddy(self.sBox_undetframes)
        self.label_blursize.setBuddy(self.sBox_blursize)
        self.label_shadow.setBuddy(self.cBox_shadow)
        self.label_foreproc.setBuddy(self.cBox_foreproc)
        self.label_erodeshape.setBuddy(self.cBox_erodeshape)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pBtn_getFile, self.pBtn_getDir)
        MainWindow.setTabOrder(self.pBtn_getDir, self.cBox_scene)
        MainWindow.setTabOrder(self.cBox_scene, self.sBox_history)
        MainWindow.setTabOrder(self.sBox_history, self.sBox_threshold)
        MainWindow.setTabOrder(self.sBox_threshold, self.sBox_area)
        MainWindow.setTabOrder(self.sBox_area, self.dsBox_ratio)
        MainWindow.setTabOrder(self.dsBox_ratio, self.cBox_erodeshape)
        MainWindow.setTabOrder(self.cBox_erodeshape, self.pBtn_getBackground)
        MainWindow.setTabOrder(self.pBtn_getBackground, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.lineEdit_videoFile)
        MainWindow.setTabOrder(self.lineEdit_videoFile, self.lineEdit_saveDir)
        MainWindow.setTabOrder(self.lineEdit_saveDir, self.sBox_cam_num)
        MainWindow.setTabOrder(self.sBox_cam_num, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.scrollArea_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视频摘要系统"))
        self.menu_menu.setTitle(_translate("MainWindow", "菜单(&M)"))
        self.menu_view.setTitle(_translate("MainWindow", "视图(&V)"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dockWidget_frame.setWindowTitle(_translate("MainWindow", "视频"))
        self.dockWidget_settings.setWindowTitle(_translate("MainWindow", "设置"))
        self.pBtn_getFile.setText(_translate("MainWindow", "选择文件"))
        self.label_videoFile.setText(_translate("MainWindow", "视频文件："))
        self.label_saveDir.setText(_translate("MainWindow", "保存目录："))
        self.pBtn_getDir.setText(_translate("MainWindow", "选择目录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vfile), _translate("MainWindow", "视频文件"))
        self.label_cam_num.setText(_translate("MainWindow", "摄像头序号："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cam), _translate("MainWindow", "实时摄像"))
        self.label_scene.setText(_translate("MainWindow", "预设场景："))
        self.cBox_scene.setItemText(0, _translate("MainWindow", "默认"))
        self.cBox_scene.setItemText(1, _translate("MainWindow", "自定义"))
        self.label_history.setToolTip(_translate("MainWindow", "用于学习背景的帧数"))
        self.label_history.setText(_translate("MainWindow", "背景参考历史帧数："))
        self.label_threshold.setToolTip(_translate("MainWindow", "用于判断当前像素是前景还是背景"))
        self.label_threshold.setText(_translate("MainWindow", "运动检测方差阈值："))
        self.label_area.setToolTip(_translate("MainWindow", "检测运动面积不小于指定值（未防噪不要设太小）"))
        self.label_area.setText(_translate("MainWindow", "运动检测面积："))
        self.label_ratio.setText(_translate("MainWindow", "背景比率："))
        self.label_interruptframes.setToolTip(_translate("MainWindow", "允许指定帧内未检测到运动的帧被摘要"))
        self.label_interruptframes.setText(_translate("MainWindow", "允许的不连续帧数："))
        self.label_blursize.setToolTip(_translate("MainWindow", "用于前景处理的滤波核尺寸"))
        self.label_blursize.setText(_translate("MainWindow", "图像滤波核尺寸："))
        self.label_autoback.setToolTip(_translate("MainWindow", "默认手动点击按钮更新"))
        self.label_autoback.setText(_translate("MainWindow", "开启自动背景更新："))
        self.label_shadow.setToolTip(_translate("MainWindow", "开启后能检测阴影并剔除阴影影响，会明显加大运算量"))
        self.label_shadow.setText(_translate("MainWindow", "开启阴影检测："))
        self.label_shadowvar.setText(_translate("MainWindow", "阴影检测阈值："))
        self.label_foreproc.setToolTip(_translate("MainWindow", "噪音较少时才开启进一步降噪"))
        self.label_foreproc.setText(_translate("MainWindow", "开启形态学处理："))
        self.label_erodeshape.setToolTip(_translate("MainWindow", "用于形态学开运算降噪,核尺寸越大越耗时"))
        self.label_erodeshape.setText(_translate("MainWindow", "腐蚀/膨胀核尺寸："))
        self.cBox_erodeshape.setToolTip(_translate("MainWindow", "用于前景处理的形态学开运算核尺寸"))
        self.cBox_erodeshape.setItemText(0, _translate("MainWindow", "(3,3)"))
        self.cBox_erodeshape.setItemText(1, _translate("MainWindow", "(5,5)"))
        self.cBox_erodeshape.setItemText(2, _translate("MainWindow", "(7,7)"))
        self.cBox_erodeshape.setItemText(3, _translate("MainWindow", "(9,9)"))
        self.cBox_erodeshape.setItemText(4, _translate("MainWindow", "(11,11)"))
        self.cBox_erodeshape.setItemText(5, _translate("MainWindow", "(13,13)"))
        self.pBtn_getBackground.setToolTip(_translate("MainWindow", "按指定帧数更新背景"))
        self.pBtn_getBackground.setText(_translate("MainWindow", "更新背景"))
        self.pBtn_showBackground.setText(_translate("MainWindow", "显示背景图片"))
        self.action_run.setText(_translate("MainWindow", "运行/继续(&R)"))
        self.action_run.setToolTip(_translate("MainWindow", "运行/继续（Ctrl+R）"))
        self.action_run.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_stop.setText(_translate("MainWindow", "停止(&T)"))
        self.action_stop.setToolTip(_translate("MainWindow", "停止（Ctrl+T)"))
        self.action_stop.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.action_pause.setText(_translate("MainWindow", "暂停(&P)"))
        self.action_pause.setToolTip(_translate("MainWindow", "暂停（Ctrl+P）"))
        self.action_pause.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_view_restore.setText(_translate("MainWindow", "重置视图(&R)"))
        self.action_view_restore.setToolTip(_translate("MainWindow", "重置视图(Ctrl+V)"))
        self.action_view_restore.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_about.setText(_translate("MainWindow", "关于(&A)"))
        self.action_about.setToolTip(_translate("MainWindow", "关于"))


