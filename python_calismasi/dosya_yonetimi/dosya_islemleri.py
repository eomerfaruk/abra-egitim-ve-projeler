



f = open("log.txt","r") # var olan dosya  okuma modunda acılır


print(f.read()) # dosyadaki bilgiler okunur ve consola yazdırılır

f.seek(0)# dosyadaki imlecin konumunu 0'a alırız

satirlar = f.readlines()  # bu fonksiyon dosyadaki satırlarda yazılan dataları satır seklinde liste elemanı yapar ve liste olusturur
print(satirlar)


f.close() # dosya kapatılır
