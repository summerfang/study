import numpy as np
from numpy.lib.shape_base import split
import pandas as pd
import matplotlib.pyplot as py
import sklearn as sk
from sklearn.metrics import mean_squared_error

df = pd.read_csv("petrol_consumption.csv")


X = [1,2,3,4,5]
Y = [1,1,2,2,4]

Y_hat = [0.6,1.29,1.99,2.69,3.4]

MSE_sklean = mean_squared_error(Y, Y_hat)
print("MSE is euqal to {0} calculated by sklearn.metrics.mean_squared_error()", MSE_sklean)

MSE_np = np.square(np.subtract(Y, Y_hat)).mean()
print("MSE is equal to {0} calculated by np", MSE_np)