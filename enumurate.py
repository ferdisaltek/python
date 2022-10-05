# m=["a","b","c"]

# obj=enumerate(m)
# print(type(obj))
# print(list(obj))

# for i in enumerate(m):
#     print(i[0])


# for index,value in enumerate(m):
#     print(index,value)



liste1 = [1,2,3,4,5]
liste2 = ['a','b','c','d','e','f']
liste3 = [100,200,300,400,500]

print(list(zip(liste1,liste2,liste3)))

for item in zip(liste1,liste2):
    print(item)

for a,b,c in zip(liste1,liste2,liste3):
    print(a,b,c)