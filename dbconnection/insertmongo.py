import pymongo  
from pymongo import MongoClient

client = MongoClient("mongodb+srv://url")
print("Connection Successful")

collection = client.libraryDB.books  
booksData = [  
  
      {  
         "id":"01",  
         "language": "Java",   
         "edition": "third",  
         "author": "Herbert Schildt"  
      },  
  
      {  
         "id":"07",  
         "language": "C++",  
         "edition": "second",  
         "author": "E.Balagurusamy"  
      }  
   ]  
  
collection.insert_many(booksData)
