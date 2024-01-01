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

def transformer_encoder(inputs, head_size, num_heads, ff_dim, dropout=0, epsilon=1e-6, attention_axes=None, kernel_size=1):
  """
  Creates a single transformer block.
  """
  x = layers.LayerNormalization(epsilon=epsilon)(inputs)
  x = layers.MultiHeadAttention(
      key_dim=head_size, num_heads=num_heads, dropout=dropout,
      attention_axes=attention_axes
      )(x, x)
  x = layers.Dropout(dropout)(x)
  res = x + inputs

    # Feed Forward Part
  x = layers.LayerNormalization(epsilon=epsilon)(res)
  x = layers.Conv1D(filters=ff_dim, kernel_size=kernel_size, activation="relu")(x)
  x = layers.Dropout(dropout)(x)
  x = layers.Conv1D(filters=inputs.shape[-1], kernel_size=kernel_size)(x)
  return x + res

def build_transfromer(head_size, num_heads, ff_dim, num_trans_blocks, mlp_units, dropout=0, mlp_dropout=0, attention_axes=None, epsilon=1e-6, kernel_size=1):
  """
  Creates final model by building many transformer blocks.
  """
  n_timesteps, n_features, n_outputs = 5, 1, 5
  inputs = tf.keras.Input(shape=(n_timesteps, n_features))
  x = inputs
  for _ in range(num_trans_blocks):
    x = transformer_encoder(x, head_size=head_size, num_heads=num_heads, ff_dim=ff_dim, dropout=dropout, attention_axes=attention_axes, kernel_size=kernel_size, epsilon=epsilon)

  x = layers.GlobalAveragePooling1D(data_format="channels_first")(x)
  for dim in mlp_units:
    x = layers.Dense(dim, activation="relu")(x)
    x = layers.Dropout(mlp_dropout)(x)

  outputs = layers.Dense(n_outputs)(x)
  return tf.keras.Model(inputs, outputs)

def fit_transformer(transformer: tf.keras.Model, data):
  """
  Compiles and fits our transformer.
  """
  transformer.compile(
    loss="mse",
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    metrics=["mae", 'mape'])

  callbacks = [tf.keras.callbacks.EarlyStopping(monitor='loss', patience=10, restore_best_weights=True)]
  start = time.time()
  hist = transformer.fit(data.X_train, data.y_train, batch_size=32, epochs=25, verbose=1, callbacks=callbacks)
  print(time.time() - start)
  return hist


def predict_a_week(tick):
    """
    Takes a ticker and predicts the next weeks prices.
    """
    data = ETL(tick)


    transformer = build_transfromer(head_size=128, num_heads=4, ff_dim=2, num_trans_blocks=4, mlp_units=[256], mlp_dropout=0.10, dropout=0.10, attention_axes=1)
    hist = fit_transformer(transformer, data)
    transformer_preds = PredictAndForecast(transformer, data.train, data.test)

    with open('holding.txt', 'a') as file:
       file.write(f'Predictions for {tick} using Transformer: {transformer_preds.predictions[-1]}\n')
       print(f'Predictions for {tick} using Transformer: {transformer_preds.predictions[-1]}\n')

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