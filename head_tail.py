import random

user_chose=input("1 or 0 \n").lower()

macine=random.randint(0,1)
print(macine)
if int(user_chose)==macine:
    print("win")
else:
    print("lost")