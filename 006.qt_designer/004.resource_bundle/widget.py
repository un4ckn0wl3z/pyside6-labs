from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_widget import Ui_Widget

import resource_rc #You need to manually import the compiled resource file

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User data")
        self.spin_box.setValue(50)
        self.increse_btn.clicked.connect(self.plus)
        self.decrese_btn.clicked.connect(self.minus)

        plus_icon = QIcon(":/images/plus-button.png")
        minus_icon = QIcon(":/images/minus-button.png")

        self.increse_btn.setIcon(plus_icon)
        self.decrese_btn.setIcon(minus_icon)


    def plus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value + 1)

    def minus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value - 1)