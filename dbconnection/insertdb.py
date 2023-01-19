import mysql
from connetion import connection

def insertCustomer(NAME,ADDRESS):
    
    cursor=connection.cursor()

    sql="INSERT INTO CUSTOMERS(NAME,ADDRESS) values(%s,%s)"
    values=(NAME,ADDRESS)

    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f'{cursor.rowcount}')
        print(f'last index {cursor.lastrowid}')
    except mysql.connector.errors as err:
        print("hata", err)
    finally:
        connection.close()
        print("database bağlantisi kapandi")

list=[]
while True:
    NAME=input("enter name : ")
    ADDRESS=input("enter address : ")

    list.append((NAME,ADDRESS))

    result=input("yeni kayit yapilacak mi : (e/h)")
    if result=='h':
        print("kayitlarını veritabanına aktariliyor")
        print(list)
        break


insertCustomer(NAME,ADDRESS)