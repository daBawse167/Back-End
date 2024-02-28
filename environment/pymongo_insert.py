from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["Imported Data"]

test_item = {
    "_id" : "10000000000000"
}

collection_name.insert_one(test_item)