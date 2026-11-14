


class Product: # self anahtar kelimesi ilgili classtan üretilen n  esne ile ilgili oldugunu belirten bir kelime 
    
    def __init__(self , name, price , isActive ): # bu classla alakalı bir nesne üretildigi zaman bu constrcutor metodu otomatik devreye girer ve calısır
        
        print("nesne olusturldu")
        self.name = name # dısardan aldıgımız argumanı constructor metodunda olusturukan nesneye ait oldugunu belirterek bu classtan üretilen herhangi bir nesne için bir değişken olucak
        self.pr = price
        self.active = isActive

p1 =Product("samsung" , 12,True)
p2 = Product("iphone",24,  True)
p3 = Product("xiaomi",34 , True)

print(p1.pr) # nesnenin 

urunler = [p1,p2,p3]

for urun  in urunler:

    if urun.active:
        print(f"urun adı :{urun.name} , urun fiyati : {urun.pr} ")





