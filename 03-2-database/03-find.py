from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

# 코딩 시작
matrix = db.movies.find_one({'title': '매트릭스'}, {'_id': False})

# print(matrix['star'])
matrix_star = matrix['star']

same_matrix = list(db.movies.find({'star': matrix_star}))

for movie in same_matrix:
    print(movie['title'])
