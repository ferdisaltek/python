# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.
# "r": okuma modu => belirtilen konumda dosya olmalıdır.

f = open("folder_path/msg.txt")
print(f)
#print(help(f))
#print(f.read())
print(f.read())

f.seek(0)

f.readline()

f.readlines()

f.close()