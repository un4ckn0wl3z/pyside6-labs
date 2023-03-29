from PySide6.QtWidgets import QApplication
from widget import Widget
import sys
import qdarktheme
from qt_material import apply_stylesheet

app = QApplication(sys.argv)
qdarktheme.setup_theme()
# apply_stylesheet(app, theme='dark_teal.xml')

widget = Widget()
widget.show()

app.exec()