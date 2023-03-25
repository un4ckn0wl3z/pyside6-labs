from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget!")

        button_1 = QPushButton("Button#1")
        button_2 = QPushButton("Button#2")

        button_1.clicked.connect(self.button_1_clicked)
        button_2.clicked.connect(self.button_2_clicked)


        button_layout = QVBoxLayout()
        button_layout.addWidget(button_1)
        button_layout.addWidget(button_2)

        self.setLayout(button_layout)
    
    def button_1_clicked(self):
        print("Button #1 clicked")

    def button_2_clicked(self):
        print("Button #2 clicked")
