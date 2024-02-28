from pymongo import MongoClient
import json5

client = MongoClient("mongodb+srv://tomH:mbWS0uIrROmONBOv@biodevice.3jz8qms.mongodb.net/")
db = client.Firebase
collection = db.Firebase_data

test_item = {
    "_id" : "10000000000000"
}

collection.insert_one(test_item)