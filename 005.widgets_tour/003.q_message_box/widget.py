from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")

        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)

        self.setLayout(layout)
    

    # the hard way (Critical)
    def button_clicked_hard(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Message title")
        message.setText("Something happened")
        message.setInformativeText("Do you want to do something about it?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")

    # Critical
    def button_clicked_critical(self):
        ret = QMessageBox.critical(self, 
                                   "Message Title",
                                   "Critical Message!",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")

    # Information
    def button_clicked_information(self):
        ret = QMessageBox.information(self, 
                                   "Message Title",
                                   "Information Message!",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")

    # Warning
    def button_clicked_warning(self):
        ret = QMessageBox.warning(self, 
                                   "Message Title",
                                   "Warning Message!",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")

    # About
    def button_clicked_about(self):
        ret = QMessageBox.about(self, 
                                   "Message Title",
                                   "About Message!")
        if ret == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Cancel")