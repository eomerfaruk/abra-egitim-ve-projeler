



sayilar = [3,5,7,2,12,34,45]


for sayi in sayilar :
    print(sayi)

for sayi in sayilar:

    if sayi % 3 == 0:
        print(str(sayi) + "3 ün katıdır")

top = 0
for sayi in sayilar:
    top = top + sayi

print(top)




###################### uygulama

urunler = [

    {"urun_adi":"HP Victus" , "fiyat": 32999},
    {"urun_adi":"Apple" , "fiyat": 25499},
    {"urun_adi":"Huawei" , "fiyat": 49999},
    {"urun_adi":"Casper" , "fiyat": 26999},
    {"urun_adi":"HP Victus-2" , "fiyat": 30999}

]



for urun in urunler:
    print(f"{urun['urun_adi']}  marka urununun fiyati {urun['fiyat']} turk lirası  ")


top = 0

for urun in urunler:

    top = top + urun["fiyat"] # fiyatalr toplanır 

print(f"ürün toplamı : {top} ")



for urun in urunler:
    if urun["fiyat"] >25000 and urun["fiyat"] <40000:
        print(f"{urun["urun_adi"]} => {urun["fiyat"]}")


kelime = input("aramak istenilen urun : ")

for urun in  urunler:
    if(urun["urun_adi"].lower().find(kelime.lower()) >-1):

        print(f"{urun['urun_adi']}")



