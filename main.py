import requests 
from bs4 import BeautifulSoup



input_date = input("What Year you would like to travel in format: YYYY-MM-DD:\n")


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}

url = "https://www.billboard.com/charts/hot-100/"+input_date

response = requests.get(url=url, headers = headers)



soup = BeautifulSoup(response.text, "html.parser")



list_100 = []
tags= soup.select("li.o-chart-results-list__item h3.c-title")
for tag in tags:
    song_title = tag.getText().strip()
    list_100.append(song_title)

print(list_100)



