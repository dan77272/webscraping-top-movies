import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
top_movies_website = response.text

soup = BeautifulSoup(top_movies_website, "html.parser")

top_movies = soup.find_all(name="h3", class_="title")
movies = []
for movie in top_movies:
    movies.append(movie.getText())

with open("top_movies.txt", "w") as file:
    for movie in movies[::-1]:
        file.write(f"{movie}\n")





