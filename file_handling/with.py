#file = open("/Users/ferdisaltek/Documents/GitHub/python/file_handling/msg.txt")
# #print(file)
# #file.close()

# with open("/Users/ferdisaltek/Documents/GitHub/python/file_handling/msg.txt") as file:
#     for i in file:
#         print(i)
#     #print(file.read(10))
#     #print(file.readline())
#     #print(file.tell()) 

try:
    with open("/folder_path/msg.txt") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("dosya okuma hatasi: ", e)
finally:
    print("dosya kapandi")
    

