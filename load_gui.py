# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from gui import Ui_MainWindow
from gui1 import Ui_Dialog


class second_screen(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.text)

    def text(self):
        print("ok")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.second_s = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.show_screen)

    def show_screen(self):
        # self.second_s = QDialog()
        # self.ui = Ui_Dialog()
        # self.ui.setupUi(self.second_s)
        # self.ui.pushButton.clicked.connect(self.text)
        # self.second_s.exec()

        self.second_s = second_screen()
        self.second_s.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())