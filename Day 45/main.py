from bs4 import BeautifulSoup

with open("./Day 45/website.html", "r", encoding="utf-8") as file:
    contents= file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup)
all_anchore_tags = soup.find_all(name ="a")
# print(all_anchore_tags)

for tag in all_anchore_tags:
    print(tag.get("href"))

heading= soup.find(name="h1", id= "name")
print(heading)

