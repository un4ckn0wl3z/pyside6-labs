from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction

class MainWindows(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # declare an app member
        self.setWindowTitle("Custom MainWindow")

        # Menu Bar
        menu_bar = self.menuBar()
        
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        # Toolsbar
        tools_bar = QToolBar("My main toolbar")
        tools_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tools_bar)

        # add action
        tools_bar.addAction(quit_action)

        # create own action
        action_1 = QAction("Some Action", self)
        action_1.setStatusTip("Status message for some action")
        action_1.triggered.connect(self.toolbar_action_1_clicked)
        tools_bar.addAction(action_1)
    
    def quit_app(self):
        self.app.quit()

    def toolbar_action_1_clicked(self):
        print("Action #1 clicked")
