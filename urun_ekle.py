#    Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

i = 0
adet = int(input('kaç adet ürün eklemek istiyorsunuz: '))
urunler = []

while (i < adet):
    urunAdi = input('ürün adi: ')
    fiyat = input('ürün fiyati: ')
    urunler.append({
        'urunAdi': urunAdi,
        'fiyat': fiyat
    })
    i += 1

# for urun in urunler:
#     print(f"ürün adı: {urun['urunAdi']} ürün fiyatı: {urun['fiyat']}")

a = 0
while (a < len(urunler)):
    print(f"ürün adi: {urunler[a]['urunAdi']} ürün fiyati: {urunler[a]['fiyat']}")
    a += 1


