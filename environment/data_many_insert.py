from pymongo import MongoClient, InsertOne
import json

client = MongoClient("mongodb+srv://tomH:mbWS0uIrROmONBOv@biodevice.3jz8qms.mongodb.net/")
db = client.Firebase_Data
collection = db.Imported_Data
requesting = []

with open(r"Readings Database Structure.jsonc") as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)
client.close()