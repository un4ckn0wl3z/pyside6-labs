from PySide6.QtWidgets import QApplication
import sys
from widget import Widget
from qt_material import apply_stylesheet
# from PySide6.QtGui import QFont


app = QApplication(sys.argv)

window = Widget()

# font = QFont()
# font.setFamily("Angsana New Bold")

# # Set the default font for all PySide6 widgets
# app.setFont(font)

# setup stylesheet
apply_stylesheet(app, theme='dark_purple.xml')

window.show()

app.exec()