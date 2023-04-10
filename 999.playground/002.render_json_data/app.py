from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMenu
from PySide6.QtCore import Qt, QEvent

class CustomTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Set the table to have no editing
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        
        # Set the line color to be transparent
        self.setStyleSheet("QTableView {border: none;}")
        
        # Set the table to be single selection
        self.setSelectionBehavior(QTableWidget.SelectRows)
        
        # Enable right-clicking on rows
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        
    def event(self, event):
        # Disable the editing of the table cells
        if event.type() == QEvent.FocusIn:
            return False
        return super().event(event)
    
    def showContextMenu(self, pos):
        menu = QMenu()
        deleteAction = menu.addAction("Delete")
        action = menu.exec(self.mapToGlobal(pos))
        if action == deleteAction:
            self.removeRow(self.currentRow())

if __name__ == "__main__":
    app = QApplication([])
    import qdarktheme
    qdarktheme.setup_theme()
    
    # Create a custom table widget
    table = CustomTableWidget()
    
    # Add rows and columns to the table
    table.setRowCount(5)
    table.setColumnCount(3)
    
    # Set the data in each cell
    item = QTableWidgetItem("1")
    table.setItem(0, 0, item)
    item = QTableWidgetItem("2")
    table.setItem(0, 1, item)
    item = QTableWidgetItem("3")
    table.setItem(0, 2, item)
    
    item = QTableWidgetItem("4")
    table.setItem(1, 0, item)
    item = QTableWidgetItem("5")
    table.setItem(1, 1, item)
    item = QTableWidgetItem("6")
    table.setItem(1, 2, item)
    
    item = QTableWidgetItem("7")
    table.setItem(2, 0, item)
    item = QTableWidgetItem("8")
    table.setItem(2, 1, item)
    item = QTableWidgetItem("9")
    table.setItem(2, 2, item)
    
    item = QTableWidgetItem("10")
    table.setItem(3, 0, item)
    item = QTableWidgetItem("11")
    table.setItem(3, 1, item)
    item = QTableWidgetItem("12")
    table.setItem(3, 2, item)
    
    item = QTableWidgetItem("13")
    table.setItem(4, 0, item)
    item = QTableWidgetItem("14")
    table.setItem(4, 1, item)
    item = QTableWidgetItem("15")
    table.setItem(4, 2, item)
    
    # Show the table
    table.show()
    
    app.exec()
