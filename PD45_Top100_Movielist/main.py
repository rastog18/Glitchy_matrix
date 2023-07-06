import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
Shetty_Endpoint = "https://api.sheety.co/671a84e3088f2b708d75aa10a672a436/top100MovieList/movies"

response = requests.get(url=URL).text
soup = BeautifulSoup(response,"html.parser")

movie_list = soup.find_all(name="h3",class_="title")
for i in range(len(movie_list)):
    movie_list[i] = movie_list[i].getText()
movie_list = movie_list[::-1]

for movie in movie_list:
    print(movie)
    # data = {"movie":{"movieName":movie}}
    # print(movie)
    # response = requests.post(url=Shetty_Endpoint,json=data)
