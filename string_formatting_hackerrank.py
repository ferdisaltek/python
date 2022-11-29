
# print("The decimal value of", dec, "is:")
# print(bin(dec), "in binary.")
# print(oct(dec), "in octal.")
# print(hex(dec), "in hexadecimal.")
# n=int(input("sayi gir"))

# for i in range(1,n+1):
#     if i==1:
#         print("1  1  1  1")
#     else:
#         print(str(i)+' '*len(bin(i)[2:])+oct(i)[2:]+' '*len(bin(i)[2:])+hex(i)[2:]+' '*len(bin(i)[2:])+bin(i)[2:].ljust(len(bin(i)[2:])))



def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, n + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
        
n=int(input(""))
print_formatted(n)