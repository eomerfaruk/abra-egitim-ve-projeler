
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow , QApplication , QAction , QWidgetAction
from PyQt5.QtGui import * 

"""
QMainWindow, uygulamanın ana penceresini oluşturmak için kullanılan bir sınıftır.

Yani kullanıcının karşısına çıkan ana uygulama ekranını oluşturmanı sağlar.
QMainWindow sana hazır bir pencere yapısı sunar. Bu pencerenin içerisine:
- Menü çubuğu (MenuBar)
- Araç çubuğu (ToolBar)
- Durum çubuğu (StatusBar)
- Ana içerik alanı (CentralWidget)
- Dock panelleri

ekleyebilirsin.
""" 

class App(QMainWindow): #  uygulama için class yapıldı QMainWindow inherit edildi
    def __init__(self): # nesne uretildiginde bu fonksiyon calısacak
        super().__init__()
        # bu classtan nesne üretildiginde otomatik olarak bu özelliklere sahip olacak
        self.baslik = "merhaba"
        self.sol = 10 
        self.ust = 10
        self.en = 640
        self.boy = 400
        self.arayuz() #nesne uretilince bu classtan bu fonksiyon calısacak 

    def arayuz(self):
        self.setWindowTitle(self.baslik) #widgetin baslıgı olusturuldu
        self.setGeometry(self.sol , self.ust , self.en , self.boy) # qidgetin baslangıc konumu ve boyutları girildi

        # widgetteki menubar kısmı olusturuldu

        anaMenu = self.menuBar() # widgetteki ust yatay bölgeye menubar olusturuldu
        fileMenu = anaMenu.addMenu("file") # file bölümü eklendi
        editMenu= anaMenu.addMenu("Edit") # edit bölümü eklendi
        viewMenu = anaMenu.addMenu("view") # view bolumu eklendi
        newProject = fileMenu.addMenu("new") # file menunun ıcıne new bolumu eklendı
        tiklamaButon = QAction("tikla"  ,self)
        newProject.addAction(tiklamaButon) # bu fonksiyon QAction nesnesini menuye veya arac cubuguna eklemek için kullanılır
        tiklamaButon.triggered.connect(self.tiklandi)
        #newProject.addAction(tiklamaButon)

        cikisButon = QAction(QIcon("bug.png") , "Cikis",self) # QAction, bir işlem (eylem) tanımlamak için kullanılan sınıftır.
                                                              # Bir menü seçeneğine tıklandığında hangi işlemin yapılacağını belirler.
        
        cikisButon.setShortcut("Ctrl+C") # kısaltma olusturulur  
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





