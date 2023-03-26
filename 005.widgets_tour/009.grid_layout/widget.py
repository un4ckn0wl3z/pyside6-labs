from PySide6.QtWidgets import QWidget, QGridLayout, QSizePolicy, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        button_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_4 = QPushButton("Four")
        button_5 = QPushButton("Five")
        button_6 = QPushButton("Six")
        button_7 = QPushButton("Seven")

        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1, 0, 0)
        grid_layout.addWidget(button_2, 0, 1, 1, 2)
        grid_layout.addWidget(button_3, 1, 0, 2, 1)
        grid_layout.addWidget(button_4, 1, 1)
        grid_layout.addWidget(button_5, 1, 2)
        grid_layout.addWidget(button_6, 2, 1)
        grid_layout.addWidget(button_7, 2, 2)

        self.setLayout(grid_layout)