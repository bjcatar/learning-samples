import pymongo

# https://realpython.com/data-engineer-interview-questions-python/

client = pymongo.MongoClient("mongodb://localhost:27017")

# Note: This database is not created until it is populated by some data
db = client["example_database"]

customers = db["customers"]
items = db["items"]

customers_data = [
  {"fisrtname": "Bob", "lastname": "Adams"},
  {"fisrtname": "Amy", "lastname": "Smith"},
  {"fisrtname": "Rob", "lastname": "Bennet"},
]
items_data = [
  {"title": "USB", "price": "10.2"},
  {"title": "Mouse", "price": "12.23"},
  {"title": "Monitor", "price": "199.99"},
]

# customers.insert_many(customers_data)
# items.insert_many(items_data)

# Just add "boughtitems" to the customer where the firstname is Bob
bob = customers.update_many(
  {"firstname": "Bob"},
  {
    "$set": {
      "boughtitems": [
        {
          "title": "USB",
          "price": 10.2,
          "currency": "EUR",
          "notes": "Customer wants it delivered via Fedex",
          "original_item_id": 1
        }
      ]
    ,}
  }
)

amy = customers.update_many(
  {"firstname": "Amy"},
  {
    "$set": {
      "broughtitems": [
        {
          "title": "Monitor",
          "price": 199.99,
          "original_item_id": 3,
          "discounted": False
        }
      ]
    },
  }
)

# print(type(amy)) # pymongo.results.UpdateResult

# Create index to speed up query
# customers.create_index([("name", pymongo.DESCENDING)])

# Retrieve customer names sorted asc
# items = customers.find().sort("name", pymongo.ASCENDING)

# Iterate through and print items
# for item in items: 
#   print(item.get('boughtitems'))

# Retrieve list of unique names
# customers.distinct("firstname")

for c in customers.find({}, {"_id": 0, "firstname": 1, "lastname": 2}):
  print(c)

print(customers.find({"firstname": "Bob"}, {"_id": 0, "firstname": 1, "lastname": 2}))

