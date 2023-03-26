from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and Images Demo")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("images/minions.png"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)