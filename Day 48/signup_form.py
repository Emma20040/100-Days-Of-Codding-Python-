from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path =r"D:\100 days of python\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)
driver= webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("EMMANUEL NKWANWI")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("FONGONG")

email = driver.find_element(By.NAME, "email")
email.send_keys("robertjones237@yahoo.com")

singup= driver.find_element(By.TAG_NAME, "button")
singup.send_keys(Keys.ENTER)

sleep(30)