import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

first_model = Sequential()
first_model.add(Dense(5, input_dim= 10, activation="relu"))
first_model.add(Dense(1, activation='sigmoid'))

first_model.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])

train_x = np.random.random(size=(6000, 10))
train_y = np.random.randint(2, size=(6000,))

val_x = np.random.random(size=(1000, 10))
val_y = np.random.randint(2, size=(1000, ))

first_model.fit(train_x, train_y, epochs=3, batch_size=64, validation_data=(val_x, val_y))