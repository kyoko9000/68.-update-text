import random
import sys
import time
from multiprocessing import Pool

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.pushButton.clicked.connect(self.start_capture_video)

        self.pushButton_1 = QtWidgets.QPushButton(self.uic.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(250, 270, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setText("Stop")

        self.pushButton_1.clicked.connect(self.stop_process)

        self.thread = {}

        # self.num_thread = 3

    def stop_process(self):
        self.thread[0].stop_select()
        self.thread[1].stop_select()
        # self.thread[2].stop_select()
        # self.thread[3].stop_select()

        # for i in range(self.num_thread):
        #     self.thread[i].stop_select()

    def start_capture_video(self):
        # for i in range(self.num_thread):
        for i in range(4):
            self.thread[i] = live_stream(index=i)
            self.thread[i].start()
            self.thread[i].signal.connect(self.show_wedcam)

    #
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
        with Pool(processes=4) as self.pool:
            self.signal.emit("run", self.index)
            # print same numbers in arbitrary order
            for i in self.pool.imap_unordered(process_work, [self.index]):
                self.signal.emit(i, self.index)

    def stop_select(self):
        print("command process stop: ", self.index)
        self.pool.terminate()
        self.signal.emit("stop", self.index)


def process_work(index):
    count = random.randint(0, 5)
    while True:
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
