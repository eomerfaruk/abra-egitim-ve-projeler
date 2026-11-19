
"""
with open("markalar.txt","a" , encoding = "utf-8") as file : # güncelleme modu 
    file.write("2.opel\n") # bu modda önce yazılan veriler silinmez altına veya yanına yaılır yeni veriler
"""




with open("markalar.txt","r+" , encoding="utf-8") as file :
    markalar = file.read() #dosyadan okunan degerler değişkene atandı
    markalar = "1 - toyota\n" + markalar
    file.seek(0) # imlec basa alınır
    file.write(markalar) # dosyaya yazılır


with open("markalar.txt","r+",encoding="utf-8") as file :
    markalar  =file .readlines() # dosyadaki verilerden liste yapılır
    markalar.insert("3 - renaul\n") # listenin sonuna eleman eklenir
    file.seek(0) # imlec basa alınır


with open("markalar.txt","r") as file :
    print(file.read())


with open("markalar.txt" , "r+",encoding="utf-8") as file :

    markalar = file.readlines() #dosyadaki  ker satirdaki veriler  liste elemanı olur

    markalar.append("mercedes\n")
    file.seek(0)
    file.writelines(markalar) # butun veriler teker teker her satıra yazılır

