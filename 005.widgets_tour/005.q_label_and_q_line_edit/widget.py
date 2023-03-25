from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QTimer, Qt
class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and QLineEdit")

        # Create a QLabel widget to display the title
        self.titleLabel = QLabel(self.windowTitle())
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setContentsMargins(10, 0, 10, 0)

        # Create a timer to update the title periodically
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTitle)
        self.timer.start(100)

        # A set of signals we can connect to
        label = QLabel("Fullname: ")
        self.line_edit = QLineEdit()
        # self.line_edit.textChanged.connect(self.text_changed)
        # self.line_edit.cursorPositionChanged.connect(self.text_cursor_pos_changed)
        # self.line_edit.editingFinished.connect(self.text_editing_finished)
        # self.line_edit.returnPressed.connect(self.text_return_pressed)
        # self.line_edit.selectionChanged.connect(self.text_selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("I AM HERE")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)
    
    # Slots
    def button_clicked(self):
        print("Fullname:", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        self.text_holder_label.setText(self.line_edit.text())

    def text_cursor_pos_changed(self, old, new):
        print("cursur old position :", old, " -new position", new)

    def text_editing_finished(self):
        print("Finished edit")
        self.line_edit.clear()
    
    def text_return_pressed(self):
        print("Return pressed")
        self.line_edit.clear()

    def text_selection_changed(self):
        print("Selection changed:", self.line_edit.selectedText())

    def text_edited(self, new_text):
        print("new text", new_text)

    def updateTitle(self):
        # Get the current window title
        currentTitle = self.windowTitle()

        # Rotate the title by one character
        newTitle = currentTitle[1:] + currentTitle[0]

        # Update the title label with the new title
        self.titleLabel.setText(newTitle)

        # Update the window title with the new title
        self.setWindowTitle(newTitle)





