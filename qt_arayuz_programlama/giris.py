import sys
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *



class window(QWidget): # arayuz penceremiz icin class sınıfı olusturuldu Qwidget sınıfı inherit edilir

    def __init__(self , parent = None ):
        super(window , self).__init__(parent)   
        self.resize(200,50)
        self.setWindowTitle(" pyqt5 derslseri ")
        self.yazi = QLabel(self)
        self.yazi.setText(" merhaba ")    
        font = QFont() # arayuze yazmak için  yazı fontu nesnesi olusturuldu
        font.setFamily("Arial") # font türü verildi
        font.setPointSize(16) # 
        self.yazi.setFont(font)
        self.yazi.move(50,20)

def main():
    app = QApplication(sys.argv)
    ekran = window()
    ekran.show()
    sys.exit(app.exec_())


def window():

    app = QApplication(sys.argv) # qt arayuz uygulaması olusturulur

    w = QWidget()  # temel arayuz (widget) olusturuldu

    yazi = QLabel(w) # w değişkenli widgeta yazi yazmak için etiket fonksiyonu nesne tanımlanır
    yazi.setText("merhaba") # yazı yazzılır

    w.setGeometry(0,0,200,50) # widgetin ekrandaki konumu ve widgetin baslangıc boyutu ayarlanır
    yazi.move(50,20) # yazı belirlenen kordınatlaraa tasınır

    w.setWindowTitle("PyQt5 dersleri") # pencere baslıgı yazılır

    w.show() # pencere cağırılır
    sys.exit(app.exec_()) # pencere calısabilmesi için systemden cıkır . 



if __name__ == '__main__': #  main fonksiyonu kısmı
    # window() # fonksiyon cağırıldı
    main()


