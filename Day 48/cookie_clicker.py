from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path =r"D:\100 days of python\chromedriver-win64\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie_click = driver.find_element(By.ID, "cookies")

number_of_clicks =1000
while number_of_clicks< 1000:

    cookie_click.click()
    

sleep(20)