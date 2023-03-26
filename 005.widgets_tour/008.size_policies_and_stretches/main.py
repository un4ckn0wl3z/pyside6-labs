from PySide6.QtWidgets import QApplication
import sys
from widget import Widget
import qdarktheme
import os
from PySide6.QtGui import QIcon


basedir = os.path.dirname(__file__)

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(basedir, 'icons', 'my_icon.ico')))

# Apply the complete dark theme to your Qt App.
qdarktheme.setup_theme()

window = Widget()
window.show()

app.exec()