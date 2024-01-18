import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.metrics import mean_absolute_percentage_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras import layers
import time
import timeit
from datetime import datetime

from ETL import ETL
from PredictAndForcast import PredictAndForecast

def build_lstm(etl: ETL, epochs=25, batch_size=32) -> tf.keras.Model:
  """
  Builds, compiles, and fits our LSTM baseline model.
  """
  n_timesteps, n_features, n_outputs = 5, 1, 5
  callbacks = [tf.keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)]
  model = Sequential()
  model.add(LSTM(200, activation='relu', input_shape=(n_timesteps, n_features)))
  model.add(Dense(50, activation='relu'))
  model.add(Dense(n_outputs))
  print('compiling baseline model...')
  model.compile(optimizer='adam', loss='mse', metrics=['mae', 'mape'])
  print('fitting model...')
  start = time.time()
  history = model.fit(etl.X_train, etl.y_train, batch_size=batch_size, epochs=epochs, validation_data=(etl.X_test, etl.y_test), verbose=1, callbacks=callbacks)
  print(time.time() - start)
  return model, history

def predict_a_week(tick):
    """
    Takes a ticker and predicts the next weeks prices.
    """
    data = ETL(tick)
    model = build_lstm(data)
    model_lstm = model[0]

    preds = PredictAndForecast(model_lstm, data.train, data.test)
    with open('holding.txt', 'a') as file:
       file.write(f'Predictions for {tick} using LSTM: {preds.predictions[-1]}\n')
       print(f'Predictions for {tick} using LSTM: {preds.predictions[-1]}\n')

with open('holding.txt', 'a') as file:
    now = datetime.now()
    print("Current date and time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    file.write(f'Current date and time: {now.strftime("%Y-%m-%d %H:%M:%S")}\n')

predict_a_week('JD')
predict_a_week('NTES')
predict_a_week('BABA')
predict_a_week('YINN')

predict_a_week('SCO')
predict_a_week('UNG')
predict_a_week('BOIL')

predict_a_week('AAL')

predict_a_week('SOXL')
predict_a_week('SOXS')

predict_a_week('TMF')

predict_a_week('PYPL')