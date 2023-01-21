import  mysql.connector
import connetion

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

mycursor.execute("select * from customers")
result=mycursor.fetchall()

for i in result:
    print(i[1])