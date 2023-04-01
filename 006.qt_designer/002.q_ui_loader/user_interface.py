from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("widget.ui", None)
        self.ui.setWindowTitle("User Data")
        self.ui.submit_btn.clicked.connect(self.do_something)

    def do_something(self):
        print(self.ui.fullname_led.text(), "as a ", self.ui.occupation_led.text())
    
    def show(self):
        self.ui.show()