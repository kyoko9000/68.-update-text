import sys
import threading
import time

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.a = 0
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.start_thread)
        # self.signal.connect(self.update_text)

    def start_thread(self):
        # self.uic.tableWidget.setItem(1, 1, QTableWidgetItem(str(self.a)))
        # self.uic.label.setText(str(self.a))

        t = threading.Thread(target=self.job)
        t.start()

    def job(self):
        while True:
            print(self.a)
            self.signal.emit(self.a)
            self.signal.connect(self.update_text)
            time.sleep(1)
            self.a += 1
            if self.a == 5:
                break

    def update_text(self):
        self.uic.tableWidget.setItem(1, 1, QTableWidgetItem(str(self.a)))
        self.uic.label.setText(str(self.a))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())