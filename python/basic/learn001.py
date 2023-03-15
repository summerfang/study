dict_example = {'name': 'Zara', 'age': 7, 'class': 'First'}

print(dict_example.get('name1', 10))

for key, value in dict_example.items():
    print(key, value)


import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = requests.get(url).text   # html text
soup = BeautifulSoup(html, 'html.parser')   # html parser
table = soup.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})   # find div tag
print(table)