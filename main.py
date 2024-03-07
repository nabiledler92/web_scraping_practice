from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

website = "https://www.adamchoi.co.uk/overs/detailed"
path = str("Users/MuhammadNabilMohdTak/Downloads/chromedriver-win64/chromedriver-win64")

#driver = webdriver.Chrome(path)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Italy')

time.sleep(5)

matches = driver.find_elements(By.TAG_NAME,'tr')

date =[]
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.cvs', index=False)
print(df)
