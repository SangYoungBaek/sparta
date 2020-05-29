# import requests
# from bs4 import BeautifulSoup

# # 타겟 URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)


# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
# soup = BeautifulSoup(data.text, 'html.parser')

# # select를 이용해서, tr들을 불러오기
# movies = soup.select('#old_content > table > tbody > tr')

# # movies (tr들) 의 반복문을 돌리기
# for movie in movies:
#     a_tag = movie.select_one('td.title > div > a')
#     b_tag = movie.select_one('td.ac > img')
#     c_tag = movie.select_one('td.point')
#     if a_tag is not None:
#         print(b_tag['alt'], a_tag.text, c_tag.text)

# from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})

# all_users = list(db.users.find())

# same_ages = list(db.users.find({'age' : 21}))

# print(all_users[0])
# print(all_users[0]['name'])

# for user in all_users:
#     print(user)

# user = db.users.find_one({'name' : 'bobby'})
# print(user)

# user = db.users.find_one({'name' : 'bobby'}, {'_id' : False})
# print(user)

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
# user = db.users.find_one({'name' : 'bobby'}, {'_id' : False})
# print(user)

# import requests
# from bs4 import BeautifulSoup

# from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# # URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup = BeautifulSoup(data.text, 'html.parser')

# # select를 이용해서, tr들을 불러오기
# movies = soup.select('#old_content > table > tbody > tr')

# # movies (tr들) 의 반복문을 돌리기
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         rank = movie.select_one('td:nth-child(1) > img')['alt'] # img 태그의 alt 속성값을 가져오기
#         title = a_tag.text                                      # a 태그 사이의 텍스트를 가져오기
#         star = movie.select_one('td.point').text                # td 태그 사이의 텍스트를 가져오기
#         doc = {
#             'rank' : rank,
#             'title' : title,
#             'star' : star
#         }
#         db.movies.insert_one(doc)


#-----------------------------------------------------------------------------
# import requests
# from bs4 import BeautifulSoup
# import string

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# soup = BeautifulSoup(data.text, 'html.parser')

# #music = soup.select("#body-content > div.newest-list > div > table > tbody > tr > a")
# # input_list = soup.select("#body-content > div.newest-list > div > table > tbody > tr > td > input")
# # for title in input_list:
# #     print(title['title'])
#     #body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number
 
# input_list = soup.select("#body-content > div.newest-list > div > table > tbody > tr")
# for title in input_list:
#     rank = title.select_one('td.number').text.split()
#     song_title = title.select_one('td.info > a.title.ellipsis').text
#     artist = title.select_one('td.info > a.artist.ellipsis').text
#     # print(rank[0], song_title[0], artist[0-1])
#     print(rank[0], song_title.strip(), artist)