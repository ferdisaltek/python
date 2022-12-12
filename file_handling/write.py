# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur. 


# file=open("file_handling/yeni_dosya.txt","w")
# file.write("dosyaya yazma islemi yapildi\n")
# file.write("dosyaya yazma islemi 2 defa yapildi")
# print(file)

with open("file_handling/yeni_dosya.txt","w") as file :
    file.write("dosyaya yazma islemi yapildi\n")
    file.write("dosyaya yazma islemi 2 defa yapildi")
    print(file)

with open("file_handling/yeni_dosya.txt","r") as file:
    print(file.read())