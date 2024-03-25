def asalsayıları_bul(sayı1,sayı2):
    for sayı in range(sayı1,sayı2+1):
        if sayı>1:
            for i in range(2,sayı):
                if (sayı% i==0):
                    break
            else:
                    print(sayı)
sayı1 =int(input("sayı1 : "))
sayı2 = int(input("sayı2 : "))
asalsayıları_bul(sayı1,sayı2)        
