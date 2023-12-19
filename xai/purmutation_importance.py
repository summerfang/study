from sklearn.datasets import fetch_california_housing
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split 

cali_house = fetch_california_housing()

print(cali_house.DESCR)

X = cali_house.data
y = cali_house.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = tf.keras.Sequential([
tf.keras.layers.Dense(40, activation=tf.nn.relu,
                              input_shape=[len(X_train[0])]),
tf.keras.layers.Dense(20, activation=tf.nn.relu),
tf.keras.layers.Dense(1)        
]) 

model.compile(optimizer = 'adam', loss = 'mse', metrics=['mse'])
model.fit(X_train, y_train, epochs = 30)