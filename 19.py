def Emeklilik_hesabı(dogum_yılı,isim) :
    yashesabı= int(dogum_yılı)

    yas = 2024-yashesabı
    emeklilik = 65-yas
    if emeklilik>0:
        print("Emekliliğinize: {emeklilik} yıl kaldı")
    else:
        print("Zaten Emeklisiniz.")
Emeklilik_hesabı(1980,"Ramo")
Emeklilik_hesabı(1900,"semih")
Emeklilik_hesabı(1943,"Yusuf")
Emeklilik_hesabı(1972,"tezcan")












