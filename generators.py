# (1 - ∞) aralığındaki her sayının karesini getiren fonksiyon.
def sonsuz_Sayi_uret():
    sayi=0
    while True:
        yield sayi
        sayi+=1

generator=sonsuz_Sayi_uret()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


