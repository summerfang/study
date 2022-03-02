import pandas as pd

stock = pd.read_csv('./MSFT.csv')

print(stock.head(10))

draw_back = 0
highest = 0
lowest = 0

draw_backs = list()

for index, row in stock.iterrows():
    highest = max(row['High'], highest)
    lowest = row['Low']

    if highest - lowest >= draw_back:
        draw_back = highest - lowest
    else:
        draw_backs.append(draw_back)

print(draw_backs)