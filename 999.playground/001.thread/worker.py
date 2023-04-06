from PySide6.QtCore import QObject, QThread, Signal
from git import Repo

class Worker(QObject):
    finished = Signal(str)
    progress = Signal(str)

    def doWork(self):
        self.progress.emit('Generating...')
        try:
            Repo.clone_from('https://github.com/un4ckn0wl3z/gladiator.git', './repo')
            self.finished.emit('Done')
        except Exception as e:
            self.finished.emit(f'Error: {str(e)}')

        