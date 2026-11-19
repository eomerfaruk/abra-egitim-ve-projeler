
"""

file = open("log.txt",encoding="utf-8") #dosya acıldı

print(file.read()) # acılan dosya okundu

file.close()# dosya kapandı
"""

"""

with open("log.txt",encoding="utf-8") as file : # file isimde dosyayı actık

    #print(file.read(10)) # 10 karakter okunur
    #print(file.tell()) # imlec  dosyadakı kacıncı karakterde oldugunu soyler

    print(file.read()) # okunan degerler str turunden olur
    file.seek(0)
    satirlar = file.readlines()
    print(satirlar)

"""

with open("log.txt" ,encoding = "utf-8") as file :

    for i in file : # satirları donguyle teker teker cekcer
        print(i)    
