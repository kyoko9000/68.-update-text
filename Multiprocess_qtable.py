import random
import sys
import time
from multiprocessing import Queue, Process

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
        for i in range(4):
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
        q = Queue()
        p = Process(target=process_work, args=(q, self.index))
        p.start()
        text = (q.get())
        self.signal.emit(text, self.index)


class process_work():
    def __init__(self, q, index):
        super().__init__()

        count = random.randint(0, 10)
        for i in range(index):
            count += 1

        print("progress", index)
        a = [count, count, count]
        print(f'value{index}', a)
        q.put(a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())