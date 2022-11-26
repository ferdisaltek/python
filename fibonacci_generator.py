def fib_lib(max):
    sayilar=[]
    a,b=0,1
    while len(sayilar)<max:
        sayilar.append(b)
        a,b=b,a+b
    return sayilar

#print(fib_lib(10))

def fib_generator(max):
    a,b=0,1
    count=0
    while count<max:
        a,b=b,a+b
        yield b
        count+=1


for i in fib_generator(100000000):
    print(i)