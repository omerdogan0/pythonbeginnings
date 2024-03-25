yeni_maas= 0
maas = input("Maasınızı giriniz: ")
zam = input("Zam oranı(%): ")
yeni_maas= int(maas)+ (int(maas)* int(zam)/100)
print("Zamlı maaş: ", yeni_maas)
