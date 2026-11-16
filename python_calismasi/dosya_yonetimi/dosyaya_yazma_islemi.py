

file = open("dosya.txt" ,"w") #yazma mounda dosya acılır yoksa o isimde dosya olusturulur daha önceden varsa dosya içeriğ silinir bos dosyada islem yapılır
file.write("omer erdem\n")# dosyaya bilgi yazılır sonra asagı satıra gecilir

file.close() # fiöe nesnesi kapatılır


with open("dosya.txt","r",encoding = "utf-8") as file: #with kelimesi otomatik olarak dosayı kapatır blok bitince
    print(file.read())
