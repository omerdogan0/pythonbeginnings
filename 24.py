sayılar= [18,22,25,15,75,85,30,32,24,27]
sayac= 0
for sayı in sayılar:
    if sayı %5==0 :
        print(str(sayı)+(" : 5'in katıdır."))
        sayac= sayac+1
    else:
        print("Döngü bitti.")
print("5 in katı olan sayı adeti : "+ str(sayac))
