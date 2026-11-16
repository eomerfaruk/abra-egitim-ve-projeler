



with open("dosya.txt","a"  , encoding  ="utf-8") as file: # dosya ekleme modunda acıldı eger dosya yoksa olusturulur
     #bu modda imleci kullanamayız
    file.write("birinci satir\n") # ekleme modundayken dosyaya bilgiyi bi sonraki imlec konumundan ekler önceki silinmez



with open("dosya.txt","r+",encoding = "utf-8") as file:
    
    print(file.read())
    file.write("yeni satir\n")



