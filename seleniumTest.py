from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

b = webdriver.Firefox()
url = "http://www.kobis.or.kr/kobis/business/stat/boxs/findFormerBoxOfficeList.do?loadEnd=0&searchType=search&sMultiMovieYn=&sRepNationCd=K&sWideAreaCd="
b.get(url)

movies = b.find_elements_by_css_selector(".boxMNm")

for movie in movies:
	movie_code = movie.get_attribute("onclick").split("'")[3]
	
	movie.click()
	
	WebDriverWait(b, 10).until(
		EC.presence_of_element_located((By.ID, movie_code + "_staff")))

	movie_staffs = b.find_elements_by_css_selector(".peopContent2")
	movie_actors = movie_staffs[0].find_elements_by_css_selector(".peopContNm")

	for actor in movie_actors:
		print(actor)

	print(movie.text, movie_code)

	b.find_element_by_class_name("layer_close").click()

b.quit()
