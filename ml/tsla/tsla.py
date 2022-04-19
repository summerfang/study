import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset_train = pd.read_csv("TSLA.csv")
dataset_train.head()

training_set = dataset_train.iloc[:,1:2].values

print(training_set)
print(training_set.shape)

