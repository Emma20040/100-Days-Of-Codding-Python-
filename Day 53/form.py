from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# selenium setup
chrome_driver_path = r"D:\100 days of python\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get('https://docs.google.com/forms/d/e/1FAIpQLSd5H6djxZJyoXY4h_9hYD5p0WIraXYlcbE3lAata7W-3wvHkw/viewform?usp=dialog')
sleep(5)
f_address =driver.find_element(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[jsname="YPqjbf"][aria-labelledby="i1 i4"]')
f_address.send_keys("address")


f_price = driver.find_element(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[jsname="YPqjbf"][aria-labelledby="i6 i9"]')
f_price.send_keys('price')

f_link = driver.find_element(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[jsname="YPqjbf"][aria-labelledby="i11 i14"]')
f_link.send_keys('ahajshas')

submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
submit.click()
# <input type="text" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="off" tabindex="0" aria-labelledby="i11 i14" aria-describedby="i12 i13" aria-disabled="false" dir="auto" data-initial-dir="auto" data-initial-value="rueireueirueirueirueirueiruierierueirueirueiruer" badinput="false">
