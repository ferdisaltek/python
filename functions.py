def toplam():
    return 10+20

sonuc = toplam() + 50

def yil():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    return yil() - 1983

sonuc = yasHesapla()

def saat():
    import datetime
    return datetime.datetime.now().hour


def selamla():
    if (saat()<12):
        return "Günaydın"
    else:
        return "Merhaba"



print(sonuc)


def selamla(isim):
    return "Merhaba, " + isim

sonuc = selamla("ferdi")
sonuc = selamla("saltek")

def toplam(a,b):
    return a + b

sonuc = toplam(10,20)
sonuc = toplam(20,30)

def yasHesapla(dogumYili):
    return 2021 - dogumYili

sonuc = yasHesapla(1983)
sonuc = yasHesapla(1993)

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas

    if kalanSure > 0:
        print(f"{isim}, emekliliğinize {kalanSure} yil kaldi.")
    else:
        print(f"{isim}, zaten {abs(kalanSure)} yil önce emekli oldunuz.")

emekliligeKacYilKaldi(1983, "ali")
emekliligeKacYilKaldi(1950, "veli")