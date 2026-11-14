

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 


def window():
    app = QApplication(sys.argv)
    ekran = QDialog()

    # buton 1 düzenlemesi
    b1 = QPushButton(ekran) # buton olusturulup ekran değişkenli widgwta atandı
    b1.setText("baslat") # buton adı baslat yaapıldı
    b1.move(20,20)# buton 20 ,20 lik kordinatlara koyuldu
    b1.clicked.connect(b1_tiklandi) # b1 butonuna tıklarsak b1_tiklandi fonksiyonuna bağlanır

    # buton 2 düzenlemesi
    b2 = QPushButton(ekran) # ekran değişken isimli widgetimize yeni bir push butonu eklendi
    b2.setText("durdur")
    b2.move(100,20) #  buton widgette 40,40lık kordiantlarda konumlanır
    b2.clicked.connect(b2_tiklandi) # b2 butonuna tıklayınca b2_tiklandi fonksiyonuna bağlanır 

    # ekran düzenlemesi
    ekran.setGeometry(100,100,200,80) # witget boyutları ve acılıs konumları ayarlandı
    ekran.setWindowTitle("merhaba") # widget ekran baslıgı olusturuldu
    ekran.show()
    sys.exit(app.exec_())

def b1_tiklandi():
    print("birinci buton baslata tiklandi")

def b2_tiklandi():
    print("ikinci buton durdura tiklandi")


if __name__ ==  '__main__':

    window()

