from PySide6.QtWidgets import QWidget,QInputDialog,QLineEdit
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from designer.ui_widget import Ui_Widget
import qdarktheme


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QPalette Demo")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
    
    
    def button_clicked(self, checked):
        print("Clicked")
        if checked:
            qdarktheme.setup_theme("light")
        else:
            qdarktheme.setup_theme()