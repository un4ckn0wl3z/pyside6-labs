from PySide6.QtWidgets import QApplication
import sys
from main_windows import MainWindows
from qt_material import apply_stylesheet


app = QApplication(sys.argv)

window = MainWindows(app)

# setup stylesheet
apply_stylesheet(app, theme='dark_teal.xml')


window.show()

app.exec()