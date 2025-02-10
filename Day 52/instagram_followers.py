from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException

chrome_driver_path = r"D:\100 days of python\chromedriver-win64\chromedriver.exe"
SERVICE = Service(chrome_driver_path)

# login info
USERNAME =''
PASSWORD =''

class InstagramFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVICE)

    def login(self):
        self.driver.get('https://www.instagram.com')
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        username.send_keys(USERNAME)
        print('step1')
        password =self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        print('step3')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
        login_button.click()
        sleep(30)
        
    def search(self):
        self.driver.get('https://www.instagram.com/chefsteps/')
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(10)

        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(10)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(10)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstagramFollower()
bot.login()
bot.search()
bot.follow()