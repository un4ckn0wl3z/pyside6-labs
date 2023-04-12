from PySide6.QtCore import Qt, QModelIndex, QIODevice, QUrl,QDir,QStringListModel
from PySide6.QtWidgets import QWidget,QFileSystemModel,QTableView,QMenu
from PySide6.QtGui import QStandardItemModel,QStandardItem,QAction
from designer.ui_widget import Ui_Widget
from tablemodel import TableModel

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Custom TableModel")


        # Create a context menu and add some actions
        menu = QMenu(self.tableView)
        copy_action = QAction("Copy", menu)
        paste_action = QAction("Paste", menu)
        menu.addAction(copy_action)
        menu.addAction(paste_action)

        # Connect the context menu to the table view
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(lambda pos: menu.exec_(self.tableView.mapToGlobal(pos)))

        self.model = TableModel()
        self.tableView.setSelectionBehavior(QTableView.SelectRows)
        self.tableView.setSelectionMode(QTableView.SingleSelection)
        self.tableView.setModel(self.model)