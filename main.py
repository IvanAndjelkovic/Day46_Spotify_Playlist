import requests 
from bs4 import BeautifulSoup



input_date = input("What Year you would like to travel in format: YYYY-MM-DD:\n")
print(input_date)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}

url = "https://www.billboard.com/charts/hot-100/"+input_date

response = requests.get(url=url, headers = headers)

print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

chart_results = soup.find_all("li", class_="o-chart-results-list__item")
for item in chart_results:
    print(item.find("h3", id="Title-of-a-story").get_text(strip=True)).strip()
