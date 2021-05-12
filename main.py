

import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from app import *


# GLOBAL
WINDOW_SIZE = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent
        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))

        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.ui.btn_minimize.clicked.connect(lambda :self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda :self.close())
        self.ui.btn_menu.clicked.connect(lambda :self.slideleftmenu())

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        self.ui.btn_home.clicked.connect(lambda :self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.btn_watch.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_watch))
        self.ui.btn_stream.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_stream))
        self.ui.btn_model.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_model))
        self.ui.btn_setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting))


        self.show()

    def slideleftmenu(self):
        width = self.ui.left_menu.width()

        if width == 50:
            newwidth = 150
        else:
            newwidth = 50

        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
