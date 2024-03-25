from random import randint
rand = randint(1,100)
sayac = 0
while True:
    sayac+=1
    sayi = int(input(" 1 ile 100 arasında değer girin(0 çıkış): "))
    if (sayi==0):
        print("Oyunu iptal ettiniz.")
        break
    elif sayi < rand:
        print("Daha yüksek bir sayı girin.")
        continue
    elif sayi > rand:
        print("Daha düşük bir sayı girin.")
        continue
    else:
        print("rastgele seçilen sayı {0}!".format(rand))
        print("tahmin sayınız {0}".format(sayac))