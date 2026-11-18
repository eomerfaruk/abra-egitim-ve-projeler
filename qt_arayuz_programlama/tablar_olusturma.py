import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QWidget,QAction , QTableWidget , QTableWidgetItem  , QVBoxLayout
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import pyqtSlot 


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt"
        self.sol = 0
        self.ust = 0
        self.en = 300
        self.boy  =200
        self.setWindowTitle(self.title)
        self.setGeometry(self.sol , self.ust , self.en , self.boy)

        











if __name__ == "__main__" :
    app = QApplication(sys.argv)
    calis = App()
    sys.exit(app.exec_())