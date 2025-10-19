import requests 
from bs4 import BeautifulSoup



input_date = input("What Year you would like to travel in format: YYYY-MM-DD:\n")
print(input_date)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}

url = "https://www.billboard.com/charts/hot-100/"+input_date

response = requests.get(url=url, headers = headers)

print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

h3_tags = soup.find_all(name='h3', id="title-of-a-story", class_="a-no-trucate")
print(h3_tags[0])