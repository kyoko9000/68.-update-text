import random
import sys
import time
from multiprocessing import Pool

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.pushButton.clicked.connect(self.start_capture_video)

        self.thread = {}

    def start_capture_video(self):
        for i in range(3):
            self.thread[i] = live_stream(index=i)
            self.thread[i].start()
            self.thread[i].signal.connect(self.show_wedcam)

    def show_wedcam(self, text, index):
        self.uic.tableWidget.setItem(index, 0, QTableWidgetItem(str(text)))
        self.uic.label.setText(str(text))


class live_stream(QThread):
    signal = pyqtSignal(object, object)

    def __init__(self, index):
        self.index = index
        print("start threading", self.index)
        super(live_stream, self).__init__()

    def run(self):
        with Pool(processes=4) as pool:
            self.signal.emit("run", self.index)
            # print same numbers in arbitrary order
            for i in pool.imap_unordered(process_work, [self.index]):
                self.signal.emit(i, self.index)


def process_work(index):
    count = random.randint(0, 5)
    for i in range(20):
        time.sleep(0.2)
        count += 1
        print("progress:", index, count)
        if count == 20:
            break
    a = [count, "finish"]
    print("progress:", index, a)
    return a


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())