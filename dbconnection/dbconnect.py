import  mysql.connector

mydb=mysql.connector.connect(

    host="localhost",
    user="root",
    password="123123123",
    database="mydatabse"
)

mycursor=mydb.cursor()
# #mycursor.execute("CREATE DATABASE mydatabse")
# mycursor.execute("show databases")

# for i in mycursor:
#     print(i)

# print(mydb) 

s=mycursor.execute("select * from customers")
print(s)