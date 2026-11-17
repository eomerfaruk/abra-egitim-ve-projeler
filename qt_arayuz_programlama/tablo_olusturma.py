

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QWidget,QAction , QTableWidget , QTableWidgetItem  , QVBoxLayout
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import pyqtSlot 


class App(QWidget):
    def __init__(self, ):
        super().__init__()

        self.title = "OMER ERDEM"
        self.sol = 0
        self.ust  =0
        self.en = 300
        self.boy= 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.sol , self.ust , self.en , self.boy)
        self.tablo_olusturma()

        # tablo yerlestirme
        self.arayuz = QVBoxLayout() #tablo için bir arayüz olusturulur . dikeyolarak tablodaki bolumleri alt alta hizalar . bi yerlesim yeri olusur . daha pencereye widgete eklenmedi
        self.arayuz.addWidget(self.tabloWidget) # tablo widgetini bu arayuze eklendi

        self.setLayout(self.arayuz) #olusturulan arayuzu widgete koyarsın tablo pencerede var olmus olur
        self.show()


    def tablo_olusturma(self):
        self.tabloWidget = QTableWidget() # tablo widgeti olusturuldu
        self.tabloWidget.setRowCount(4) # tablo widgetine 4 satır konulacak
        self.tabloWidget.setColumnCount(2) # tablo widgetine 2 sutun konulacak
        
        # butun satır sutun yerlerine item koyuldu
        self.tabloWidget.setItem(0,0,QTableWidgetItem("No : 0,0"))  
        self.tabloWidget.setItem(0,1,QTableWidgetItem("No : 0,1"))
        self.tabloWidget.setItem(1,0,QTableWidgetItem("No : 1,0"))
        self.tabloWidget.setItem(1,1,QTableWidgetItem("No : 1,1"))
        self.tabloWidget.setItem(2,0,QTableWidgetItem("No : 2,0"))
        self.tabloWidget.setItem(2,1,QTableWidgetItem("No : 2,1"))
        self.tabloWidget.setItem(3,0,QTableWidgetItem("No : 3,0"))
        self.tabloWidget.setItem(3,1,QTableWidgetItem("No : 3,1"))

        self.tabloWidget.move(0,0)

        # tabloya komut 

        self.tabloWidget.doubleClicked.connect(self.tiklama)


    def tiklama(self):

        # tablo konumu içindeki itemleri for ile yakalar
        for tablokonum in self.tabloWidget.selectedItems(): 
            print(tablokonum.row() , tablokonum.column() , tablokonum.text())



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    calis = App()
    sys.exit(app.exec_())
