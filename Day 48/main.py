from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chrome_driver_path= r"D:\100 days of python\chromedriver-win64\chromedriver.exe"


service= Service(chrome_driver_path)
driver= webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

serch_bar = driver.find_element(By.NAME, "q")
# events = driver.find_elements(By.XPATH, ("//*[@id="content"]/div/section/div[2]/div[2]/div/ul"))
events_time = driver.find_elements(By.CSS_SELECTOR, "div.event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, "div event-widget li a")
dict_= {}

for elements in range(len(events_time)):
    dict_[elements] ={
        "time": events_time[elements].text,
        "name": event_name[elements].text
    }
print(dict)

print(serch_bar.tag_name)
driver.implicitly_wait(10)


sleep(30)

# driver.close()

# print(driver.title)
