"""
from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked():
    print("You clicked the button, didn't you!")


app = QApplication()
button = QPushButton("Press Me")

button.clicked.connect(button_clicked)

button.show()
app.exec()


"""


"""

from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked(data):
    print("You clicked the button, didn't you!: ", data)


app = QApplication()
button = QPushButton("Press Me")
button.setCheckable(True)

button.clicked.connect(button_clicked)

button.show()
app.exec()

"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider


def response_to_slider(data):
    print("slider moved to : ", data)

app = QApplication()

slider = QSlider(Qt.Orientation.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(response_to_slider)
slider.show()

app.exec()
