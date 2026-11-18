



sayilar = [1,2,3,4,56,778,990,76]

for sayi in sayilar:
    print(sayi)



isimler = ["ali" ,"mehmet" , "omer"]
for isim in isimler:
    print(isim)



for i in range(10): # 0 ile 9 arası for döngüsü
    print(i)


isim = "ömer erdem"

for i in isim:
    print(i)



my_tuple = [(1,2) , (3,4) , (5,6)]

for a in my_tuple:
    print(a)



for a , b in my_tuple:
    print(a , b)

my_dict = {"41":"kocaeli" , "53":"rize" , "35":"izmir"}

for x in my_dict:
    print(x) # sözlük yapısının anahtarları döner


for d in my_dict:
    print(my_dict[d])


for d in my_dict.values():# bu döngüde sözlük yapısının sadece degerleri döner
    print(d)


for x in  my_dict.keys():
    print(x)


for x in my_dict.items(): # sözlük teki key valuesler döngüde tuple seklinde alırız
    print(x)
