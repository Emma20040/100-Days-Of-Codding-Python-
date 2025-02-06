from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

driver_path =r"D:\100 days of python\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4117276611&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom')

signin_link = driver.find_element(By.LINK_TEXT, "Sign in")
signin_link.send_keys(Keys.ENTER)

email = driver.find_element(By.NAME, "session_key")
email.send_keys("emmanuelfongong10@gmail.com")

password = driver.find_element(By.NAME, "session_password")
password.send_keys("emmnkw04")

signin =driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[4]')
signin.click()

easy_apply =driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/div')
easy_apply.click()

# phone_number = driver.find_element(By.XPATH, '//*[@id="ember979"]/div/div[2]/form/div/div/div[4]')
# phone_number.send_keys("678209349")
# sleep(30)
next1= driver.find_element(By.ID, 'ember1049')
print(next1.text)
next1.click()

next2 = driver.find_element(By.LINK_TEXT, 'Next')
next2.click()

sleep(30)
sql_experience =driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4117276611-12027175122-numeric"]')
sql_experience.send_keys("2")

oracledb_exp= driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4117276611-12027175130-numeric"]')
oracledb_exp.send_keys("2")

unix_exp = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4117276611-12027175114-numeric"]')
unix_exp.send_keys("2")

review = driver.find_element(By.XPATH, '//*[@id="ember354"]/span')
review.click()

summit_application= driver.find_element(By.XPATH, '//*[@id="ember756"]/span')
summit_application.click()

sleep(20000)


# next1 ='//*[@id="ember511"]/span'
# phone_number ='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4117276611-12027175106-phoneNumber-nationalNumber"]'
# next2 ='//*[@id="ember511"]/span'
# unix ='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4117276611-12027175114-numeric"]'
# oracledb= '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4117276611-12027175130-numeric"]'
# sql= '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4117276611-12027175122-numeric"]'
# review ='//*[@id="ember354"]/span'
# summit_application ='//*[@id="ember756"]/span'