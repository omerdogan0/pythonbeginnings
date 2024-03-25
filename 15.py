toplam = 0
sayı1 = input("1. sayıyı giriniz: ")
sayı2 = input("2.sayıyı giriniz: ")
for i in range(int(sayı1)+1,int(sayı2)):
    toplam+=i
print("{0} ile {1} arasındaki sayıların toplamı: {2}".format(sayı1,sayı2,toplam))
