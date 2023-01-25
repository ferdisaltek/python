import pymongo  
from pymongo import MongoClient

client = MongoClient("mongodb+srv://ferdisaltek:XDSKWhU236acPQbR@cluster0.tgyhn.mongodb.net/node-app?retryWrites=true&w=majority")
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