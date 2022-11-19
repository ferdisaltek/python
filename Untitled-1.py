#Kullanıcıdan herhangi bir veri girmesini istiyoruz
#sayı = input("Herhangi bir veri girin: ")

#Kullanıcının girdiği verinin tipini bir
#değişkene atıyoruz
#tip = type(sayı)

#Son olarak kullanıcının girdiği verinin tipini
#ekrana basıyoruz.
#print("Girdiğiniz verinin tipi: ", tip)


#--------------------------------------------condition

# import random_control

# print(random_control.x)

# markalar = []

# marka = input("marka: ")
# markalar.append(marka)

# marka = input("marka: ")
# markalar.append(marka)

# marka = input("marka: ")
# markalar.append(marka)

# print(markalar)



# a=[0,1,2,3]
# print(a[-1])
# for a[-1] in a:
#     print(a[-1])


# if __name__ == '__main__':
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print(sorted(list(set(arr)))[-2])

    


def split_and_join(line):
    #print(line.split())
    a=line.split()
    #print(a)
    a="-".join(a)
    print(a)

    

split_and_join("this is a string   ")