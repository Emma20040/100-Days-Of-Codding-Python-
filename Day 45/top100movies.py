import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# all_movies = soup.find_all(name="span", class_="content_content__i0P3p")
all_movies = soup.find_all(name="h2")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
print(movies)

with open("./Day 45/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")