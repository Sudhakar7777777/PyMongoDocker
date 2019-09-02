import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["customers_db"]
customers = db["customers"]

for x in customers.find():
    print(x)