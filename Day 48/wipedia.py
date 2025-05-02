from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"D:\100 days of python\chromedriver-win64\chromedriver.exe"
service= Service(chrome_driver_path)
driver= webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count=  driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[1]/a')
# article_count.click()
# print(article_count.text)

# clicking on a link on the page
link = driver.find_element(By.LINK_TEXT, "view history")
# link.click()

# serching using text 
serach = driver.find_element(By.NAME, "search")
serach.send_keys("python")
serach.send_keys(Keys.ENTER)

sleep(30)
