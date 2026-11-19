markalar = ["opel","bmw","togg"]


index = 1

obj1 = enumerate(markalar) # listeyi enumarete sınıflı bir değişkene dönüstürdük

print(obj1)
print(type(obj1))


print(list(obj1)) # enumerate :  listedeki elemanları ikili tuple sekline (eleman liste numarası , eleman degeri) olusturmus



for marka in enumerate(markalar):
    print(marka)



for index , value in enumerate(markalar,1): # liste numaralandırması 1den baslar
    print(f"{index} - {value}")



"""
zip : iki listeyi birlestiren fonksiyondur

"""    



numara = [100,200,300]
ogrenci = ["ali","mehmet","omer"]


my_list = list(zip(numara , ogrenci)) #zip ve enumerate for dısında kullanılırsa listeye donusturulerek kullanılır

print(my_list) # zip iki listenin ilk degerlerini olusturdugu listenin ikiki tuple ı  


for ogr in zip(numara , ogrenci):
    print(ogr)


