from pymongo import MongoClient
import json5

client = MongoClient("mongodb+srv://tomH:mbWS0uIrROmONBOv@biodevice.3jz8qms.mongodb.net/")
# Creates the list collection // 
collection = client['Firebase_data']
print(type(collection))
# Read and parse JSONC file
with open('environment/readings_data.jsonc', 'r') as f:
    jsonc_data = f.read()

# Split JSONC data into individual JSON objects
json_data_list = jsonc_data.split('\n\n')

# Insert each JSON object into MongoDB
for json_data_str in json_data_list:
    # Skip empty lines or lines with only comments
    if json_data_str.strip() == "" or json_data_str.strip().startswith("//"):
        continue
    # Parse JSON data
    json_data = json5.loads(json_data_str)
    # Insert data into MongoDB
    print(json_data)
    # collection.insert_one([json_data])
    category_index = collection.create_index("category")
print("Data inserted successfully into MongoDB")