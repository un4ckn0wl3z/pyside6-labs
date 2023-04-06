from PySide6.QtCore import QObject, QThread, Signal

class Worker(QObject):
    finished = Signal()
    progress = Signal(int)

    def doWork(self):
        for i in range(100):
            # Simulate some long-running task
            self.progress.emit(i)
            QThread.sleep(1)

        self.finished.emit()