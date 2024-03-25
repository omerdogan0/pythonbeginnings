secim= input("Sinema için(1),Tiyatro için (2) tuşlayınız: ")
öğrenci= input("Öğrenci misinizi(E/H): ")
ücret = 0

if secim =='1':
    ücret= 15

elif secim== '2':
    ücret = 10

if öğrenci=='E'or öğrenci=='e':
    ücret=ücret/2
print("ödemeniz gerekn ücret :{}".format(ücret))
