
urunler = [
    {'name':'iphone 8', 'price': '4000' },
    {'name':'iphone 8 Plus', 'price': '5000' },
    {'name':'iphone X', 'price': '6000' },
    {'name':'iphone XR', 'price': '7000' },
    {'name':'iphone 11', 'price': '8000' },
    {'name':'samsung s10', 'price': '6000' },
]



# 4- Kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz.

kelime = input('aramak istediğiniz ürün: ')

for urun in urunler:
    if (urun['name'].find(kelime.lower()) > -1):
        print(f"ürün adi: {urun['name']} ürün fiyati: {urun['price']}")

