import sys

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader


loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("widget.ui", None)

def do_something():
    print(window.fullname_led.text(), "is a ", window.occupation_led.text())


window.setWindowTitle("User data")

window.submit_btn.clicked.connect(do_something)
window.show()
app.exec()