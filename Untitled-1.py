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

    


# def split_and_join(line):
#     #print(line.split())
#     a=line.split()
#     #print(a)
#     a="-".join(a)
#     print(a)

    

# split_and_join("this is a string   ")

# <<<<<<< HEAD


# s = input()
# print(any(c.isalnum() for c in s))
# print(any(c.isalpha() for c in s))
# print(any(c.isdigit() for c in s))
# print(any(c.islower() for c in s))
# print(any(c.isupper() for c in s))

    



# # print(s.isalnum())
# # print(s.isalpha())
# # print(s.isdigit())
# # print(s.islower())
# # print(s.isupper())





# =======
# def print_full_name(first, last):
#     print(f"Hello {first} {last}! You just delved into pyton")


# print_full_name(input("first :"),input("last:"))
# >>>>>>> 71d4c12 (iterator and generator)



#-------------------------------------------------------------------------
# N=11
# # M=33
# # for i in range(1, N, 2):
# #     print(str('.|.' * i).center(M, '-'))

# print("se"+' '*10+"lam")



# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)

# outer(10)



def usalma(number):
    def inner(power):
        return number ** power
    
    return inner

two = usalma(2) # 2-3
three = usalma(3) # 3-4

print(two(3))
print(three(4))