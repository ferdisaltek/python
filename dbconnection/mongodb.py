
from pymongo import MongoClient

client = MongoClient("mongodb+srv://ferdisaltek:<password>@cluster0.tgyhn.mongodb.net/?retryWrites=true&w=majority")
print("Connection Successful")
for db in client.list_databases():
    print(db)
client.close()