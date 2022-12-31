# ************************** man hinh loai 2 *************************
import sys
import time

# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.i = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.run_app)

    def run_app(self):
        self.i = "start app"
        self.update_status()
        time.sleep(2)
        self.i = "stop app"
        self.update_status()

        # for self.i in range(5):
        #     self.update_status()
        #     time.sleep(1)

    def update_status(self):
        self.uic.label.setText(str(self.i))
        self.uic.label.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())