import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=4"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

name = soup.find_all(class_='js-tile-link')

title = []
date  = []
rating = []
for i in range(len(name)):
    title.append(name[i].find(class_='p--small').get_text())
    date.append(name[i].find(class_='smaller').get_text())
Movie = pd.DataFrame({
                        'Movie Name'                                :                       title,
                        'Release Date'                              :                       date,
                    })

print(Movie)

# Movie.to_csv('TopRatedMovies.csv')