import requests
from bs4 import BeautifulSoup
import string

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
songs = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

for song in songs:
    # rank = song.select_one('td.number').split()
    rank = song.select_one('td.number').contents[0].strip()
    songTitle = song.select_one('td.info > a.title.ellipsis').text.strip()
    starName = song.select_one('td.info > a.artist.ellipsis').text
    print(rank, songTitle, starName)
