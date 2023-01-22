from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': 0}})
