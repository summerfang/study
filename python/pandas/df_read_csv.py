import pandas as pd

card_tab = pd.read_csv('./card_tab.csv')
start_train = pd.read_csv('./start_train.csv')
start_test = pd.read_csv('./start_test.csv')

print(type(card_tab))
print(card_tab.head(10))