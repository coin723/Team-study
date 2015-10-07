import urllib
from bs4 import BeautifulSoup

html = urllib.urlopen("http://comic.naver.com/webtoon/weekdayList.nhn?week=sun")
soup = BeautifulSoup(html, "html.parser")

toons = soup.find_all('strong', attrs = {'class': 'subject'})

for toon in toons:
	print toon['title']