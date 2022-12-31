# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from gui import Ui_MainWindow
from gui1 import Ui_Dialog


class second_gui(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.jj)

    def jj(self):
        print("it run")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.s = None
        self.ui = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.load_ui)

    def load_ui(self):
        self.ui = second_gui()
        self.ui.exec()
    #     self.ui = QDialog()
    #     self.s = Ui_Dialog()
    #     self.s.setupUi(self.ui)
    #     self.s.pushButton.clicked.connect(self.hh)
    #     self.ui.exec()
    #
    # def hh(self):
    #     print("ok")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
