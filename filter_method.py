liste=[1,5,18,44,33,67]

x=list(filter(lambda a: a>15, liste))
print(x)

y=list(filter(lambda i: i%2==0,liste))
print(y)

print(sorted(liste))