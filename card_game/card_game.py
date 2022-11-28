from random import shuffle

class Kart:

    def __init__(self,tip,deger):
        self.tip=tip
        self.deger=deger
        
    # def kartGetir(self):
    #     return f"{self.tip} , {self.deger}"

    def __repr__(self):
        return f"{self.tip} , {self.deger}"


# sinek5 = Kart("sinek","5")
# karoAs = Kart("karo","A")

# print(sinek5.kartGetir())
# print(karoAs.kartGetir())

# print(sinek5)
# print(karoAs)


# Deste sınıfı

# kart tipleri   => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K

# Deste sınıfındaki kartlar listesine 52 kartı for ve list comphension ile ekleyiniz.


class Deste:
    tipler = ["karo","sinek","kupa","maça"]
    degerler = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.kartlar = [Kart(tip,deger) for tip in Deste.tipler for deger in Deste.degerler]
        #print(self.kartlar)

    def kartSayisi(self):
        return len(self.kartlar)

    def kartlariKaristir(self):
        if (self.kartSayisi()<52):
            raise ValueError("Deste bozulmadan kartları karıştırabilirsiniz.")
        shuffle(self.kartlar)

    def kartDagit(self,adet):
        kartSayisi = self.kartSayisi()
        if kartSayisi == 0:
            raise ValueError("Bütün kartlar dağitildi.")
        adet = min([kartSayisi,adet])
        kartlar = self.kartlar[-adet:]
        self.kartlar = self.kartlar[:-adet]
        return kartlar

    def kartAt(self):
        return self.kartDagit(1)[0]

deste1 = Deste()

deste1.kartlariKaristir()

print(deste1.kartAt())

print(deste1.kartDagit(5))
print(deste1.kartlar)
print(deste1.kartSayisi())
print(deste1.kartDagit(3))
print(deste1.kartSayisi())

print(deste1.kartlar)
