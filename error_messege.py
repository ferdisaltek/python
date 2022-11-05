
try:
    x=int(input('x: '))
    y=int(input('y: '))
    print(x+y)
except:
    print("unkowon error")



try:
    x=int(input('x :'))
    y=int(input('y :'))
    print(x/y)
except(ZeroDivisionError,ValueError) as e:
    print("error")
    print(e)
except:
    print("unkonw error")