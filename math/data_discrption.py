import random
import statistics
import pandas as pd
import numpy as np

R30 = [random.randrange(1, 100, 1) for i in range(30)]
print(R30)

df = pd.DataFrame(list(R30))

print(df)
print(df.iloc[:][0].describe())

# List to DataFrame
list1 = ['Summer', 'John', 'Ellen']
list2 = [1,2,3]
list3 = ['F','M','F']

df3list = pd.DataFrame(list(zip(list1, list2, list3)), columns = ['Name', 'Age', 'Gender'])
print(df3list)
print('\n')

# Dictionary to DataFrame
dictStudent = {'Name': ['John', 'Anna', 'Smith'], 
               'Age': [1,2,3]}

dfStu = pd.DataFrame(dictStudent)
print(dfStu)

# Numpy array to DataFrame


# Get a list from a DataFrame
lst = dfStu['Name']
print(lst)
print(lst.to_list())
print(type(lst))
print('\n')

# Get an array from a DataFrame
print('Get an array from a DataFrame\n')

ages = df3list.iloc[:,1]
print(ages)
print(type(ages))
print("\n")
ages = df3list.iloc[:]['Age']
print(ages)
print('\n')
print(type(ages))