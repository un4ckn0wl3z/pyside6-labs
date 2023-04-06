import sys

from PySide6 import QtWidgets
from widget import Widget

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

window = Widget()
window.show()

app.exec()