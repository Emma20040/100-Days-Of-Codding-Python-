from twilio.rest import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY ="J8FH0Q53C50GV9X8"
NEWS_API_KEY ="7a8bce9b727c484a92a1e97d036d61bc"
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

   

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params= stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for(key, value) in data.items()]
yesterday_data =data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(response.json())


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

up_down = None
if abs(difference) > 0:
      up_down = "🔺"
else:
    up_down = "🔻"

    

diff_percent = (difference/ float(yesterday_closing_price)) * 100

if diff_percent > 4:
    news_params ={
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params= news_params)
    articles = news_response.json()["articles"]
    print("get news")
  
three_articles = articles[:3]

    


formatted_article = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \n Brief: {article['description']}" for article in three_articles ]

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_="+15075026348",
            to="+237678209349"
        )
 


