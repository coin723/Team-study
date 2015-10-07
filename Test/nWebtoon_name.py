import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("http://comic.naver.com/webtoon/weekdayList.nhn?week=sun")
soup = BeautifulSoup(html, "html.parser")
# def has_title(tag):
#     return tag.has_attr('title')
def dayView(tag):
	return tag.parent.name == "dt" and tag.contents[0].name != "strong"
webtoons = soup.find_all(dayView)

for webtoon in webtoons:
	print(webtoon["title"])