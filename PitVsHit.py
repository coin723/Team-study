from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

b = webdriver.Firefox()
url = "http://www.koreabaseball.com/Record/Etc/HitVsPit.aspx"
b.get(url)

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
	elif sel == "table":
		WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.tData.tt thead tr th")))
		WebDriverWait(b, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.tData.tt tbody tr td")))
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

def ifDataExist():
	return b.find_element_by_css_selector("table.tData.tt tbody tr td").get_attribute("colspan") == None

def concate(str1, str2):
	return str1 + str2

assignEle("pTeams")
for x in range(1, len(pTeams)):
	pTeams[x].click()
	prepFor("pitchers")

	for y in range(1, len(pitchers)):
		pitchers[y].click()
		prepFor("hTeams")
		prepFor("pTeams")

		for z in range(1, len(hTeams)):

			if pTeams[x].get_attribute("value") != hTeams[z].get_attribute("value"):
				hTeams[z].click()
				prepFor("hitters")

				for w in range(1, len(hitters)):
					hitters[w].click()
					prepFor("btnSearch")
					btnSearch.click()
					waitToLoad("table")

					if ifDataExist():
						prepFor("pTeams")
						prepFor("pitchers")
						prepFor("hTeams")
						prepFor("hitters")
						print("[" + pTeams[x].get_attribute("text") + "] " + 
							pitchers[y].get_attribute("text") + 
							" vs. " + 
							"[" + hTeams[z].get_attribute("text") + "] " + 
							hitters[w].get_attribute("text"))
						tHeads = b.find_elements_by_css_selector("table.tData.tt thead tr th a")
						tHeadsStr = ""
						for tHead in tHeads:
							tHeadsStr = tHeadsStr + tHead.get_attribute("title") + ",\t"
						tBodies = b.find_elements_by_css_selector("table.tData.tt tbody tr td")
						tBodiesStr = ""
						for tBody in tBodies:
							tBodiesStr = tBodiesStr + tBody.get_attribute("innerHTML") + ",\t"
						print(tHeadsStr)
						print(tBodiesStr)
					prepFor("hitters")
				prepFor("hTeams")
				prepFor("pTeams")
			prepFor("pitchers")
	prepFor("pTeams")