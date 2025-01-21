from bs4 import BeautifulSoup
import requests

response= requests.get("https://news.ycombinator.com/news")
yc_webpage =response.text 

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title)

article_tag = soup.find_all(name="span", class_= "sitebit comhead")
article_text = article_tag.getText()
article_link= article_tag.get("href")
article_upvote = soup.find(name="span", class_= "score").getText()

largest_vote = max(article_upvote)
print(largest_vote)
# 
print(article_text)
print(article_link)
print(article_upvote)