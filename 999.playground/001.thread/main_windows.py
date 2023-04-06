from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize, QThread
from PySide6.QtGui import QAction, QIcon

from worker import Worker



class MainWindows(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # declare an app member
        self.setWindowTitle("Custom MainWindow")
        self.setMinimumSize(1280, 500)
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

        action_2 = QAction(QIcon("start.png"),"Some Action", self)
        action_2.setStatusTip("Status message for some action")
        action_2.triggered.connect(self.toolbar_action_2_clicked)
        tools_bar.addAction(action_2)

        tools_bar.addSeparator()
        click_here_button = QPushButton("Click here")
        tools_bar.addWidget(click_here_button)


        # working with status bar
        self.setStatusBar(QStatusBar(self))


        button_1 = QPushButton("Button#1")
        button_1.clicked.connect(self.button_1_action_clicked)
        self.setCentralWidget(button_1)


        self._worker_thread = QThread()
        self._worker = Worker()
        self._worker.moveToThread(self._worker_thread)
        self._worker_thread.started.connect(self._worker.doWork)
        self._worker.progress.connect(self.on_progress)
        self._worker.finished.connect(self.on_finished)
        
    
    def quit_app(self):
        self.app.quit()

    def toolbar_action_1_clicked(self):
        print("Action #1 clicked")
        self.statusBar().showMessage("Message from Action#1", 3000)


    def toolbar_action_2_clicked(self):
        print("Action #2 clicked")
        self.statusBar().showMessage("Message from Action#2", 3000)

    def button_1_action_clicked(self):
        print("Button #1 clicked")
        # self.statusBar().showMessage("Message from Button #1 Action", 3000)
        self._worker_thread.start()
        self.setDisabled(True)


    def on_progress(self, value):
        self.statusBar().showMessage(f"Progress: {value}%", 0)

    def on_finished(self):
        self.setDisabled(False)
        self._worker_thread.quit()
        self._worker_thread.wait()
        self.statusBar().showMessage(f"Done", 5000)

    def closeEvent(self, event):
        self._worker_thread.quit()
        self._worker_thread.wait()
        event.accept()
