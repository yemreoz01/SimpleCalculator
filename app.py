from math import *
from time import *
print("PROJE İÇİN GELİŞTİRİLEN HESAP MAKİNESİDİR.\t writed by Yunus Emre Özdemir")
yazi ="""*************************
Hesap Makinesi v1.0
Aşağıdaki seçeneklerden birini seçiniz.
Lütfen küçük harfle giriş yapınız.
a)Toplama
b)Çıkarma
c)Çarpma
d)Bölme
e)Kök alma
f)Kare alma
g)Büyüğe yuvarlama
h)Küçüğe yuvarlama
i)Faktöriyel alma
j)Üs alma
k)Pi sayısı
l)e sayısı
q)çıkış
***************************
Hangi işlemi yapmak istiyorsunuz (Harflerle girin!) :
"""

while True:
    key = input(yazi)
    if (key == "q"):
        print("Çıkış yapılıyor ...")
        sleep(1)
        break
    elif (key == "a"):
        sayi1 = int(input("Toplama için ilk değer :"))
        sayi2 = int(input("Toplama için ikinci değer :"))
        print(sayi1+sayi2)
        sleep(2)
    elif (key == "b"):
        sayi3 = int(input("Çıkarma için ilk değer :"))
        sayi4 = int(input("Çıkarma için ikinci değer :"))
        print(sayi3+sayi4)
        sleep(2)
    elif (key == "c"):
        sayi5 = int(input("Çarpma için ilk değer :"))
        sayi6 = int(input("Çarpma için ikinci değer :"))
        print(sayi5*sayi6)
        sleep(2)
        continue
    elif (key == "d"):
        sayi7 = int(input("Bölme için ilk değer :"))
        sayi8 = int(input("Bölme için ikinci değer :"))
        print(sayi7/sayi8)
        sleep(2)
    elif (key == "e"):
        sayi9 = int(input("Kökü alınacak sayı :"))
        print(sayi9 ** 0.5)
        sleep(2)
    elif (key == "f"):
        sayi10 = int(input("Karesi alınacak sayı :"))
        print(sayi10 ** 2)
        sleep(2)
    elif (key == "g"):
        sayi11 = float(input("Büyük değere yuvarlanacak sayıyı girin (lütfen ondalıklı girin) :"))
        print(ceil(sayi11))
        sleep(2)
    elif (key == "h"):
        sayi12 = float(input("Küçük değere yuvarlanacak sayıyı girin (lütfen ondalıklı girin) :"))
        print(floor(sayi12))
        sleep(2)
    elif (key == "i"):
        sayi13 = int(input("Faktöriyeli gösterilecek sayıyı girin :"))
        print(factorial(sayi13))
        sleep(2)
    elif (key == "j"):
        sayi14 = int(input("Üssü alınacak değer :"))
        sayi15 = int(input("Kuvvet değeri :"))
        print(pow(sayi14,sayi15))
        sleep(2)
    elif (key == "k"):
        print(pi)
        sleep(2)
    elif (key == "l"):
        print(e)
        sleep(2)



















