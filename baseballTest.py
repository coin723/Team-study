from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

b = webdriver.Firefox()
url = "http://www.koreabaseball.com/Record/Etc/HitVsPit.aspx"
b.get(url)

#pTeams = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlPitcherTeam").find_elements_by_tag_name("option")

# for x in xrange(1, 11):
# 	pTeams[x].click()

def waitToLoad(sel):
	WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.tData.tt")))
	if sel == "pitchers":
		WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#cphContainer_cphContents_ddlPitcherPlayer")))
	elif sel == "hitters":
		WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#cphContainer_cphContents_ddlHitterPlayer")))
	elif sel == "pTeams":
		WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#cphContainer_cphContents_ddlPitcherTeam")))
	elif sel == "hTeams":
		WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#cphContainer_cphContents_ddlHitterTeam")))
	elif sel == "btnSearch":
		WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#cphContainer_cphContents_btnSearch")))
	return

def assignEle(sel):
	if sel == "pTeams":
		global pTeams
		pTeams = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlPitcherTeam").find_elements_by_tag_name("option")
	elif sel == "pitchers":
		global pitchers
		pitchers = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlPitcherPlayer").find_elements_by_tag_name("option")
	elif sel == "hTeams":
		global hTeams
		hTeams = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlHitterTeam").find_elements_by_tag_name("option")
	elif sel == "hitters":
		global hitters
		hitters = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlHitterPlayer").find_elements_by_tag_name("option")
	elif sel == "btnSearch":
		global btnSearch
		btnSearch = b.find_element_by_css_selector("input#cphContainer_cphContents_btnSearch")
	return

def prepFor(sel):
	waitToLoad(sel)
	assignEle(sel)

#print(pTeams[2].get_attribute("value"))

assignEle("pTeams")
for x in range(1, len(pTeams)):
	print(pTeams[x].get_attribute("value"))
	pTeams[x].click()
	prepFor("pitchers")
	# WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.tData.tt")))
	# WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#cphContainer_cphContents_ddlPitcherPlayer")))
	# pitchers = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlPitcherPlayer").find_elements_by_tag_name("option")
	# pTeams = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlPitcherTeam").find_elements_by_tag_name("option")
	for y in range(1, len(pitchers)):
		pitchers[y].click()
		prepFor("hTeams")
		# print(pitchers[y].get_attribute("value"))
		# WebDriverWait(b 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#cphContainer_cphContents_ddlHitterTeam")))
		# hTeams = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlHitterTeam").find_elements_by_tag_name("option")
		for z in range(1, len(hTeams)):
			if pTeams[x].get_attribute("value") != hTeams[z].get_attribute("value"):
				hTeams[z].click()
				# WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.tData.tt")))
				# WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#cphContainer_cphContents_ddlHitterPlayer")))
				# hTeams = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlHitterTeam").find_elements_by_tag_name("option")
				# print(hTeams[z].get_attribute("value"))
				# hitters = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlHitterPlayer").find_elements_by_tag_name("option")
				prepFor("hitters")
				for w in range(1, len(hitters)):
					hitters[w].click()
					# print(hitters[w].get_attribute("value"))
					# btnSearch = b.find_element_by_css_selector("input#cphContainer_cphContents_btnSearch")
					prepFor("btnSearch")
					# if b.find_element_by_css_selector("table.tData.tt tbody tr td").get_attribute("colspan") != None:
	prepFor("pTeams")
		# pitchers = b.find_element_by_css_selector("select#cphContainer_cphContents_ddlPitcherPlayer").find_elements_by_tag_name("option")
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

