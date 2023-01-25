
from pydoc import cli
from pymongo import MongoClient

myclient = MongoClient("mongodb+srv://ferdisaltek:<password>@cluster0.tgyhn.mongodb.net/node-app?retryWrites=true&w=majority")
print("Connection Successful")

mydb=myclient["node-app"]
mycollection=mydb["products"]

product={"name":"samsung s20","price":5}
result=mycollection.insert_one(product)
myclient.close()