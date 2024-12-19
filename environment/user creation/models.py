import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://tomH:mbWS0uIrROmONBOv@biodevice.3jz8qms.mongodb.net/")
db = client["your_database"]
collection = db["user_accounts"]

collection_list = collection.find().to_list()

usernames = [i["username"] for i in collection_list]
emails = [i["email"] for i in collection_list]

users = {"usernames":usernames, "emails":emails}

#checks for duplicate username
def duplicate_user(input_username):
    if input_username in users["usernames"]:
        return "invalid"
    else:
        return "valid"
    
#checks for duplicate email
def duplicate_email(input_email):
    if input_email in users["emails"]:
        return "invalid"
    else:
        return "valid"