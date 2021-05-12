# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets

import traffic_app_icon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(63, 46, 136);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(self.centralwidget)
        self.main_header.setMinimumSize(QtCore.QSize(0, 60))
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 70))
        self.main_header.setStyleSheet("QFrame{\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-bottom: 1px solid #000\n"
"}")
        self.main_header.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title = QtWidgets.QFrame(self.main_header)
        self.title.setStyleSheet("")
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.title)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.top_left_menu = QtWidgets.QFrame(self.title)
        self.top_left_menu.setMaximumSize(QtCore.QSize(50, 70))
        self.top_left_menu.setStyleSheet("\n"
"QPushButton:hover{\n"
"    background-color: rgb(0,92,157);\n"
"}\n"
"QPushButton{\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"    color: #fff;\n"
"    background-color: #000;\n"
"}\n"
"QFrame{\n"
"    background-color: #000;\n"
"}")
        self.top_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_left_menu.setObjectName("top_left_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.top_left_menu)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_menu = QtWidgets.QPushButton(self.top_left_menu)
        self.btn_menu.setMaximumSize(QtCore.QSize(16777215, 65))
        self.btn_menu.setStyleSheet("")
        self.btn_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/icons/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(24, 24))
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout_4.addWidget(self.btn_menu)
        self.horizontalLayout_5.addWidget(self.top_left_menu)
        self.title_bar = QtWidgets.QFrame(self.title)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.title_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout_5.addWidget(self.title_bar)
        self.horizontalLayout_2.addWidget(self.title)
        self.top_right_btns = QtWidgets.QFrame(self.main_header)
        self.top_right_btns.setMinimumSize(QtCore.QSize(100, 0))
        self.top_right_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.top_right_btns.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0,92,157);\n"
"}\n"
"")
        self.top_right_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_right_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_right_btns.setObjectName("top_right_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_minimize = QtWidgets.QPushButton(self.top_right_btns)
        self.btn_minimize.setMaximumSize(QtCore.QSize(36, 36))
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_minimize.setMouseTracking(True)
        self.btn_minimize.setStyleSheet("")
        self.btn_minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/icons/cil-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setIconSize(QtCore.QSize(24, 24))
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_3.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.top_right_btns)
        self.btn_close.setMaximumSize(QtCore.QSize(36, 36))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_close.setStyleSheet("")
        self.btn_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/icons/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QtCore.QSize(24, 24))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout_2.addWidget(self.top_right_btns)
        self.verticalLayout.addWidget(self.main_header)
        self.main_content = QtWidgets.QFrame(self.centralwidget)
        self.main_content.setStyleSheet("")
        self.main_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_content.setLineWidth(0)
        self.main_content.setObjectName("main_content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_content)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_menu = QtWidgets.QFrame(self.main_content)
        self.left_menu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    padding: 10px 10px;\n"
"    border-radius: 10px;\n"
"    color: #fff;\n"
"    background-color: #000;\n"
"}\n"
"QFrame{\n"
"    background-color: #000;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0,92,157);\n"
"}")
        self.left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu.setObjectName("left_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.left_menu_top_button = QtWidgets.QFrame(self.left_menu)
        self.left_menu_top_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_top_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_top_button.setObjectName("left_menu_top_button")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_top_button)
        self.formLayout.setContentsMargins(0, 10, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.btn_home = QtWidgets.QPushButton(self.left_menu_top_button)
        self.btn_home.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet("background-image: url(:/icons/resources/icons/cil-home.png)  ;\n"
"background-repeat: none;\n"
"background-position: center left;\n"
"padding-left: 50px;\n"
"\n"
"")
        self.btn_home.setObjectName("btn_home")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btn_home)
        self.btn_watch = QtWidgets.QPushButton(self.left_menu_top_button)
        self.btn_watch.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_watch.setFont(font)
        self.btn_watch.setStyleSheet("background-image: url(:/icons/resources/icons/cil-camera.png);\n"
"background-repeat: none;\n"
"background-position:center  left;\n"
"padding-left: 50px;\n"
"\n"
"")
        self.btn_watch.setObjectName("btn_watch")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_watch)
        self.btn_stream = QtWidgets.QPushButton(self.left_menu_top_button)
        self.btn_stream.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_stream.setFont(font)
        self.btn_stream.setStyleSheet("background-image: url(:/icons/resources/icons/cil-medical-cross.png);\n"
"background-repeat: none;\n"
"background-position:center  left;\n"
"padding-left: 50px;\n"
"")
        self.btn_stream.setObjectName("btn_stream")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_stream)
        self.btn_model = QtWidgets.QPushButton(self.left_menu_top_button)
        self.btn_model.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_model.setFont(font)
        self.btn_model.setStyleSheet("background-image: url(:/icons/resources/icons/cil-3d.png);\n"
"background-repeat: none;\n"
"background-position: center  left;\n"
"padding-left: 50px;\n"
"")
        self.btn_model.setObjectName("btn_model")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btn_model)
        self.verticalLayout_2.addWidget(self.left_menu_top_button)
        self.btn_setting = QtWidgets.QPushButton(self.left_menu)
        self.btn_setting.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_setting.setFont(font)
        self.btn_setting.setStyleSheet("background-image: url(:/icons/resources/icons/cil-settings.png);\n"
"background-repeat: none;\n"
"background-position:center  left;\n"
"padding-left: 50px;\n"
"")
        self.btn_setting.setObjectName("btn_setting")
        self.verticalLayout_2.addWidget(self.btn_setting)
        self.horizontalLayout.addWidget(self.left_menu)
        self.main_stacked = QtWidgets.QFrame(self.main_content)
        self.main_stacked.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_stacked.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_stacked.setLineWidth(0)
        self.main_stacked.setObjectName("main_stacked")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_stacked)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -1, 951, 611))
        self.stackedWidget.setStyleSheet("background-color: rgb(243, 250, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.label = QtWidgets.QLabel(self.page_home)
        self.label.setGeometry(QtCore.QRect(210, 210, 381, 141))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_home)
        self.page_watch = QtWidgets.QWidget()
        self.page_watch.setObjectName("page_watch")
        self.label_2 = QtWidgets.QLabel(self.page_watch)
        self.label_2.setGeometry(QtCore.QRect(290, 220, 381, 141))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_watch)
        self.page_stream = QtWidgets.QWidget()
        self.page_stream.setObjectName("page_stream")
        self.label_3 = QtWidgets.QLabel(self.page_stream)
        self.label_3.setGeometry(QtCore.QRect(280, 220, 381, 141))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_stream)
        self.page_model = QtWidgets.QWidget()
        self.page_model.setObjectName("page_model")
        self.tableWidget = QtWidgets.QTableWidget(self.page_model)
        self.tableWidget.setGeometry(QtCore.QRect(90, 50, 511, 192))
        self.tableWidget.setMaximumSize(QtCore.QSize(511, 192))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.stackedWidget.addWidget(self.page_model)
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setObjectName("page_setting")
        self.label_5 = QtWidgets.QLabel(self.page_setting)
        self.label_5.setGeometry(QtCore.QRect(280, 180, 381, 141))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_setting)
        self.horizontalLayout.addWidget(self.main_stacked)
        self.verticalLayout.addWidget(self.main_content)
        self.main_footer = QtWidgets.QFrame(self.centralwidget)
        self.main_footer.setMinimumSize(QtCore.QSize(0, 50))
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_footer.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.main_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_footer.setObjectName("main_footer")
        self.verticalLayout.addWidget(self.main_footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_home.setText(_translate("MainWindow", "HOME"))
        self.btn_watch.setText(_translate("MainWindow", "WATCH"))
        self.btn_stream.setText(_translate("MainWindow", "STREAM"))
        self.btn_model.setText(_translate("MainWindow", "MODEL"))
        self.btn_setting.setText(_translate("MainWindow", "SETTING"))
        self.label.setText(_translate("MainWindow", "HOME PAGE"))
        self.label_2.setText(_translate("MainWindow", "WATCH PAGE"))
        self.label_3.setText(_translate("MainWindow", "STREAM PAGE"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Source"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        self.label_5.setText(_translate("MainWindow", "SETTING PAGE"))
