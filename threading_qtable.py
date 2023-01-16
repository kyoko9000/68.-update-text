import sys
import threading
import time

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.a = 0
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.jj)

    def jj(self):
        t = threading.Thread(target=self.hh)
        t.start()

    def hh(self):
        while True:
            print(self.a)
            self.signal.emit(self.a)
            self.signal.connect(self.update1)
            time.sleep(1)
            self.a += 1
            if self.a == 5:
                break

    def update1(self):
        self.uic.tableWidget.setItem(1, 1, QTableWidgetItem(str(self.a)))
        self.uic.label.setText(str(self.a))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
