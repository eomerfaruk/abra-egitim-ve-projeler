

with open("markalar.txt","a") as file : # güncelleme modu 
    file.write("1.opel\n")


with open("markalar.txt","r+" , encoding="utf-8") as file :
    markalar = file.read() #dosyadan okunan degerler değişkene atandı
    markalar = "1 - toyota\n" + markalar
    file.seek(0) # imlec basa alınır
    file.write(markalar) # dosyaya yazılır


with open("markalar.txt","r+",encoding="utf-8") as file :
    markalar  =file .readlines() # dosyadaki verilerden liste yapılır
    markalar.insert("3 - renaul\n")
    file.seek(0)


with open("markalar.txt","r") as file :
    print(file.read())






