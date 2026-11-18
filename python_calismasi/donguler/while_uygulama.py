
devammi = "e"

ogrenciler = []

while (devammi != "h"):

    ogrenciNo = int(input("ogrenci no :"))
    ogrenciAdi = input("ogrenci adi :")
    ogrenciSoyad = input("ogrenci soyad : ")

    # bilgileri listeye sozluk yapısıyla ekledik 
    ogrenciler.append({
            "ogrenci no":ogrenciNo,
            "ogrenci adi": ogrenciAdi,
            "ogrenci soyadi":ogrenciSoyad
    })

    devammi = input("devammı ? (e/h)")

    
for ogrenci in ogrenciler:
    print(f"{ogrenci['ogrenci no']} numarali ogrencini adi {ogrenci['ogrenci adi']} {ogrenci['ogrenci soyadi']} ")





