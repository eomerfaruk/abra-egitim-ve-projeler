




def not_gir():
    ad = input("ögrenci adi :")
    soyad = input("ögrenci soyadi : ")
    not1 = input(" not 1 : ")
    not2 = input("not 2 : ")
    not3 = input("not 3 : ")

    with open("sinav_notlari.txt" , "a",encoding="utf-8") as file :
        file.write(ad + " " + soyad + " : " + not1 + " , " + not2 +" , "+ not3)

def notlari_oku():
    with open("sinav_notlari.txt","r", encoding="utf-8") as file :
        for satir in file:
            print(satir)

def notlari_kaydet():
    pass


while True:

    islem = input("1 - not gir\n 2- notları oku\n 3- notlari kayit et\n4 - cikis")

    if islem == "1":
        not_gir()

    elif islem == "2":
        notlari_oku()

    elif islem == "3":
        notlari_kaydet()

    else:
        break





