# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)
import resource_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(198, 79)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 160, 56))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.spin_box = QSpinBox(self.widget)
        self.spin_box.setObjectName(u"spin_box")

        self.verticalLayout.addWidget(self.spin_box)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.increse_btn = QPushButton(self.widget)
        self.increse_btn.setObjectName(u"increse_btn")
        icon = QIcon()
        icon.addFile(u":/images/plus-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.increse_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.increse_btn)

        self.decrese_btn = QPushButton(self.widget)
        self.decrese_btn.setObjectName(u"decrese_btn")
        icon1 = QIcon()
        icon1.addFile(u":/images/minus-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.decrese_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.decrese_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.increse_btn.setText(QCoreApplication.translate("Widget", u"Increase", None))
        self.decrese_btn.setText(QCoreApplication.translate("Widget", u"Decrease", None))
    # retranslateUi

