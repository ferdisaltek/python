
x = int(input("sayi 1 :"))
y = int(input("sayi 2 :"))
z = int(input("sayi 3 :"))
n = int(input("n değeri : "))
stuck=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                stuck.append([i,j,k])

print(stuck)

