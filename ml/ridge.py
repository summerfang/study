from os import read
from pandas import read_csv
from pandas.core.indexes.period import PeriodIndex

df = read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv', header=None)
print(df.shape)
print(df.head(10))

