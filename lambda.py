#multiply=lambda a:a**2

#prsonuc=multiply(5)
#print(prsonuc)



def myFunc(n):
    return lambda a: a * n

multiply2 = myFunc(2)
multiply3 = myFunc(10)

#sonuc = multiply2(10)
#sonuc = multiply2(20)
sonuc = multiply3(10)

print(sonuc)