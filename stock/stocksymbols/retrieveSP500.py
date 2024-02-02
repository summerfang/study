import requests
from bs4 import BeautifulSoup
import csv

url = "https://stockanalysis.com/list/sp-500-stocks/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", {"id": "main-table"})
rows = table.find_all("tr")

with open("sp500_stocks.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    for row in rows:
        cols = row.find_all("td")
        cols = [col.text.strip() for col in cols]
        writer.writerow(cols)
