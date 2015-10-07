from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

b = webdriver.Firefox()
url = "http://www.koreabaseball.com/Record/Etc/HitVsPit.aspx"
b.get(url)

pTeams = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlPitcherTeam").find_elements_by_tag_name("option")
# btnSearch = b.find_element_by_css_selector("input[type='submit']")


# for x in xrange(1, 11):
# 	pTeams[x].click()



#print(pTeams[2].get_attribute("value"))
for x in range(1, len(pTeams)):
	# print(pTeams[x].get_attribute("value"))
	pTeams[x].click()
	WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.tData.tt")))
	WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#cphContainer_cphContents_ddlPitcherPlayer")))
	pitchers = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlPitcherPlayer").find_elements_by_tag_name("option")
	for y in range(1, len(pitchers)):
		pitchers[y].click()
		# print(pitchers[y].get_attribute("value"))
		# WebDriverWait(b 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#cphContainer_cphContents_ddlHitterTeam")))
		hTeams = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlHitterTeam").find_elements_by_tag_name("option")
		for z in range(1, len(hTeams)):
			hTeams[z].click()
			WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.tData.tt")))
			WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#cphContainer_cphContents_ddlHitterTeam")))
			hTeams = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlHitterTeam").find_elements_by_tag_name("option")
			# print(hTeams[z].get_attribute("value"))
			hitters = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlHitterPlayer").find_elements_by_tag_name("option")
			for w in range(1, len(hitters)):
				hitters[w].click()
				# print(hitters[w].get_attribute("value"))
		pitchers = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlPitcherPlayer").find_elements_by_tag_name("option")
	pTeams = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlPitcherTeam").find_elements_by_tag_name("option")
	# print(pTeams[x].get_attribute("value"))
# pTeams[1].click()
# pTeams = b.find_element_by_css_selector("[name='ctl00$ctl00$cphContainer$cphContents$ddlPitcherTeam']").find_elements_by_tag_name("option")
# pTeams[2].click()

# for pTeam in pTeams:
# 	pTeam.click()
# 	pTeams = b.find_element_by_css_selector("[name='ctl00$ctl00$cphContainer$cphContents$ddlPitcherTeam']").find_elements_by_tag_name("option")
# 	print(pTeam.get_attribute("value"))

	# WebDriverWait(b, 10)
	# pitchers = b.find_element_by_css_selector("[name='ctl00$ctl00$cphContainer$cphContents$ddlPitcherPlayer']").find_elements_by_tag_name("option")
	# for pitcher in pitchers:
	# 	print(pitcher.get_attribute("value"))
	# WebDriverWait(b, 10)

	# print(pitchers[1].get_attribute("value"))
	# for hTeam in hTeams:
	# 	print(hTeam.get_attribute("value"))
	# 	hTeam.click()
	# 	WebDriverWait(b, 10)
	# 	hitters = b.find_element_by_css_selector("[name='ctl00$ctl00$cphContainer$cphContents$ddlHitterPlayer']").find_elements_by_tag_name("option")
	# 	for pitcher in pitchers:
	# 		pitcher.click()
	# 		WebDriverWait(b, 10)
	# 		for hitter in hitters:
	# 			hitter.click()
	# 			srchBtn.click()
	# 			WebDriverWait(b, 10)



# print(pTeams[1].get_attribute("value"))
# pTeams[1].click()

