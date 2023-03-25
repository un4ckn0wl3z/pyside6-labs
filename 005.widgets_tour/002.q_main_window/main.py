from PySide6.QtWidgets import QApplication
import sys
from main_windows import MainWindows


app = QApplication(sys.argv)

window = MainWindows(app)
window.show()

app.exec()