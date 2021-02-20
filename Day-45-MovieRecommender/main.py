from bs4 import BeautifulSoup
import requests

timeout = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"
response = requests.get(timeout).text
soup = BeautifulSoup(response,'html.parser')

movies = soup.find_all(name='h3', class_="card-title")
for movie in movies:
    with open('BestMoviesOfAllTime.txt','a') as f:
        f.write(movie.getText().strip()+"\n")