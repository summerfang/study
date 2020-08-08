from bs4 import BeautifulSoup
import requests

url_wiki_usa_governor = "https://en.wikipedia.org/wiki/List_of_United_States_governors"
req__wiki_usa_governor = requests.get(url_wiki_usa_governor)

soup = BeautifulSoup(req__wiki_usa_governor.text, "html.parser")
tbody = soup.tbody

for child in tbody:
    print(child.td.)