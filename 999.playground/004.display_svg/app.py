from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.bg = QFrame()
        self.bg.setStyleSheet("background-color: #333")
        self.bg_layout = QVBoxLayout(self.bg)
        file = "SVG_Logo.svg"
        self.svg_widget = QSvgWidget(file)
        self.bg_layout.addWidget(self.svg_widget)
        self.setCentralWidget(self.bg)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
