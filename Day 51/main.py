from  time import sleep
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

PROMISED_DOWN = 150
PROMISED_UP = 60
chrome_driver_path = r"D:\100 days of python\chromedriver-win64\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.speedtest.net/result/17352434216')

test_button = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
test_button.click()

sleep(70)
download_speed_element =driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
download_speed =download_speed_element.text
print(f"///////////{download_speed}")

upload_speed_element =driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload_speed = upload_speed_element.text
print(f"///////{upload_speed}")

# x.com login info
username = "CryptoTech237"
password =""

driver.get('https://x.com')
sleep(30)
sign_in = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')
sign_in.click()

sleep(30)
username_input = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')
username_input.send_keys(username)

next =driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]')
next.click()

password_input = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_input.send_keys(password)

login = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div/button')
login.click()

tweet_compose = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
tweet = f"Hey Internet Provider, why is my internet speed {download_speed}down/{upload_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
tweet_compose.send_keys(tweet)
sleep(3)
tweet_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
tweet_button.click()
        

sleep(400)