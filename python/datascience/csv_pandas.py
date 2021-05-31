import pandas as pd

df = pd.read_csv('test.csv', index_col="city", nrows=10)
print(df)

df1 = pd.read_csv('test.csv', usecols=[1,2,3], nrows=10)
print(df1)

df2 = pd.read_csv('test.csv', usecols=['city'], nrows=10)
print(df2)

f = lambda x : int(x) + 1
df3 = pd.read_csv("test.csv", converters={"training_hours":f}, nrows=10)
print(df3)

df3.filter([])