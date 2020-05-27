from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

## 코딩 할 준비 ##

movieName = list(db.movies.find({'title':'매트릭스'}, {'_id':False}))
print(movieName[0]['star'])

valus = movieName[0]['star']

same_movie = list(db.movies.find({'star' : valus}, {'_id':False}))
for movie_title in same_movie:
    print(movie_title['title'])

db.movies.update_many({'star' : valus}, {'$set' : {'star' : 0}})

count_movie = db.movies.find({ 'star' : {'$gt':'9.38'}}).count()
print(count_movie)

# 생김새
# db.people.update_many(찾을조건,{ '$set': 어떻게바꿀지 })
# same_ages = list(db.users.find({'age':21},{'_id':False}))
# all_users = list(db.users.find())
# db.articles.find( { “likes”: { $lte: 30 } } )