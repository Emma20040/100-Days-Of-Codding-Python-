import requests
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
# form ='https://docs.google.com/forms/d/e/1FAIpQLSd5H6djxZJyoXY4h_9hYD5p0WIraXYlcbE3lAata7W-3wvHkw/viewform?usp=dialog'

# i have to selenium instead of beautifulsoup because the html is rendered by javascripts
driver.get(r'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D')
# sleep(30)
# response = requests.get(URL)
# house_info = response.text

# Get the page source after JavaScript rendering
html_source = driver.page_source

soup = BeautifulSoup(html_source, "html.parser")

# price
price = soup.find_all('span', attrs={"data-test": "property-card-price"})
house_price =[prices.getText() for prices in price]
house_price=[n.split('/') for n in house_price]
flattened_list = [item for sublist in house_price for item in sublist if item not in ['mo', '1 bd']]
print(flattened_list)
# price_list =[]
# for price in house_price:
#      if price not in ['mo', '1 bd']:
#           price_list.append(price)
# print(price_list)

# print(house_price)

# address
get_address = soup.find_all('address', attrs={"data-test": "property-card-addr"})
addresses = [addr.getText() for addr in get_address]
print(addresses)

# links 
get_links = soup.find_all('a', attrs={"data-test": "property-card-link"})
links = [link.get('href') for link in get_links]
print(links)

sleep(5)
min_length = min(len(flattened_list), len(addresses), len(links))
# filling the gogle form 
i = 0


while i < min_length:
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSd5H6djxZJyoXY4h_9hYD5p0WIraXYlcbE3lAata7W-3wvHkw/viewform?usp=dialog')
    
    for address in addresses:
        f_address =driver.find_element(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[jsname="YPqjbf"][aria-labelledby="i1 i4"]')
        # input_=address 
        f_address.send_keys(address)
    
    for price in house_price:
        f_price = driver.find_element(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[jsname="YPqjbf"][aria-labelledby="i6 i9"]')
        f_price.send_keys(price)

    for link in links:
        f_link = driver.find_element(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[jsname="YPqjbf"][aria-labelledby="i11 i14"]')
        f_link.send_keys(link)

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    
    i +=1
sleep(30)
spreed_sheet= ''

