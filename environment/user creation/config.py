import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://tomH:mbWS0uIrROmONBOv@biodevice.3jz8qms.mongodb.net/")
db = client["your_database"]
collection = db["user_accounts"]

collection_list = collection.find().to_list()

def add_user(details):
    account = {
        "username": details[0],
        "email": details[1],
        "password": details[2],
        "verified": False
    }
    result = collection.insert_one(account)