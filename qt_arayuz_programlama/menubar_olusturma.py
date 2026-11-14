
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow , QApplication , QWidget , QAction  , QPushButton  , QWidgetAction
from PyQt5.QtGui import * 


class App(QMainWindow): #  uygulama için class yapıldı QMainWindow inherit edildi
    def __init__(self):
        super().__init__()
        # bu classtan nesne üretildiginde otomatik olarak bu özelliklere sahip olacak
        self.baslik = "merhaba"
        self.sol = 10 
        self.ust = 10
        self.en = 640
        self.boy = 400
        self.arayuz() # nesne uretildiginde bu class calısacak

    def arayuz(self):
        self.setWindowTitle(self.baslik)
        self.setGeometry(self.sol , self.ust , self.en , self.boy)

        anaMenu = self.menuBar()
        fileMenu = anaMenu.addMenu("file")
        editMenu= anaMenu.addMenu("Edit")
        viewMenu = anaMenu.addMenu("view")
        newProject = fileMenu.addMenu("new")
        tiklamaButon = QAction("tikla"  ,self)
        newProject.addAction(tiklamaButon)
        tiklamaButon.triggered.connect(self.tiklandi)
        newProject.addAction(tiklamaButon)

        cikisButon = QAction(QIcon("bug.png") , "Cikis",self)
        cikisButon.setShortcut("Ctrl+C") #
        cikisButon.setStatusTip("uygulamayı kapat") # buton basınca bilgilendirme verir
        cikisButon.triggered.connect(self.close) # buton aktiflestirildiginde close aktif olur oraya baglanır
        fileMenu.addAction(cikisButon)
        self.show()

    def tiklandi(self):
        print("tiklandi")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    calis = App()
    sys.exit(app.exec_())





