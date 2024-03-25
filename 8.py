print("Vücut Kitle Endeksi Hesaplama")

boy =input("Boy m: ")
kilo = input("Kilo kg: ")

endeks = float(kilo)/(float(boy)*float(boy))

if endeks < 20 :
    print("\n zayıf KE : {}".format(endeks))
elif endeks > 20 :
    print("\n kilolu KE : {}".format(endeks))
elif endeks > 25:
    print("\n Aşırı kilolu KE : {}",format(endeks))
elif endeks > 30:
    print("\n Obez KE : {}".format(endeks))






