# Import the components we need
from PySide6.QtWidgets import QApplication, QWidget

# sys module for processing command-line args
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

# start event-loop
app.exec()