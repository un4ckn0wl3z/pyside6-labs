from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtWidgets import QApplication, QTableView
import json
import sys
import qdarktheme


class TableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data
        self._header = ["Name", "Age", "City"]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._header)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return str(self._data[row][self._header[col].lower()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._header[section]
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qdarktheme.setup_theme(custom_colors={"primary": "#D0BCFF"})
    # Load JSON data from file
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Create table model and view
    model = TableModel(data)
    table_view = QTableView()
    table_view.setSelectionBehavior(QTableView.SelectRows)
    table_view.setModel(model)

    # Show table view
    table_view.show()

    sys.exit(app.exec())
