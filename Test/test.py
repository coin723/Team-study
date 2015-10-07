import urllib
from bs4 import BeautifulSoup

html = urllib.urlopen("http://www.kobis.or.kr/kobis/business/stat/boxs/findFormerBoxOfficeList.do?loadEnd=0&searchType=search&sMultiMovieYn=&sRepNationCd=K&sWideAreaCd=")
soup = BeautifulSoup(html, "html.parser")
movies = soup.find_all('a', attrs = {'class': 'boxMNm'})

for movie in movies:
	print movie['title']