from PySide6.QtWidgets import QApplication
import sys
from widget import Widget
import qdarktheme
import os
from PySide6.QtGui import QIcon
from qt_material import apply_stylesheet

app = QApplication(sys.argv)
 
# Apply the complete dark theme to your Qt App.
# qdarktheme.setup_theme()
apply_stylesheet(app, theme='dark_teal.xml')
window = Widget()
window.show()

app.exec()