from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# website to scrape and define the path
website = "https://www.audible.com/newreleases?ref_pageloadid=OlVllX47mek0nmtx&ref=a_adblbests_t1_navTop_pl0cg1c0r2&pf_rd_p=334a4a9c-12d2-4c3f-aee6-ae0cbc6a1eb0&pf_rd_r=G97M2ZS7K3HN63G18NNR&pageLoadId=pn80rFD9YdZkB6dd&creativeId=7ba42fdf-1145-4990-b754-d2de428ba482"
path = str("Users/MuhammadNabilMohdTak/Downloads/chromedriver-win64/chromedriver-win64")

#creating a webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(website)
driver.maximize_window()

# creating pagination
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

current_page = 1

# creating empty lists to store the data
book_title = []
book_author = []
book_length = []
book_price = []

# scraping the data
while current_page <= last_page:
    # wait for the page to load hence we use time.sleep
    #time.sleep(2)
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container')))
    #container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')
    #products = container.find_elements(By.XPATH,'./li')
    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located((By.XPATH, './/li[contains(@class, "productListItem")]')))
    #products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')

    for product in products:
        book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)
        book_price.append(product.find_element(By.XPATH, './/p[contains(@id, "buybox-regular-price")]').text)
    try:
        current_page = current_page + 1
        next_page = driver.find_element(By.XPATH, './/span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length, 'price': book_price})
df_books.to_csv('audible_pagination_wait_books.csv', index=False)