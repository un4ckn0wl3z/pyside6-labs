from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Widget!")

        button = QPushButton("Clicked")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def button_clicked(self):
        print("button_clicked")

    def button_pressed(self):
        print("button_pressed")

    def button_released(self):
        print("button_released")