import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import os

def get_wave_point(df: pd.DataFrame, point_chosen: str):
    if point_chosen.lower() in ['high', 'low', 'open', 'close']:
        df['wave_point'] = df[point_chosen.lower()]
        return df['wave_point']
    else:
        # Iterate throught the rows of the dataframe reverse order
        # and find the wave point
        # if previous high is lowers than the current high, then the current wave point is high
        # if previous high is higher than the current high, then the current wave point is low
        # if previous high is equal to the current high, then compare the low. If low-
        return df[point_chosen.lower()]

def extract_features_from_wave_point(df: pd.DataFrame):
    # Iterate through the rows reverse order to extract features
    # 1. Find consecutive high and low
    # 2. Find the distance between the high and low

    lst_consecutive_direction = np.array([len(df)])
    lst_directions = np.array([len(df)], 0)  # -1 means the previous wave point is lower than the current wave point, 0 means equal, 1 means higher
    lst_distance = np.array([len(df)], 0) # distance to the previous wave high or low
    lst_tick = np.array([len(df)], 0) # number of ticks between the previous wave high or low


    for i in range(len(df)-1, 0, -1):
        lst_directions[i] = df['']
        for j in range(len(df)-1, i, -1):
            pass

dir_path = os.path.dirname(os.path.realpath(__file__))

df_spy_min = pd.read_csv(f'{dir_path}/SPY_1min_sample.txt', sep=',', header=None)
df_spy_min.columns = ['Date Time', 'open', 'high', 'low', 'close', 'volume']

last_high_list = []

close_prices = df_spy_min['close'].to_numpy()
len_of_close_prices = len(close_prices)
turn_point_prices = []
if len_of_close_prices > 1:
    revserse_direction_is_up = (close_prices[len_of_close_prices-2] > close_prices[len_of_close_prices-1])

last_turn_price = close_prices[-1]
for i in range(len(close_prices) - 2, -1, -1):
    if close_prices[i] == last_turn_price: continue
    if close_prices[i] > last_turn_price:
        if revserse_direction_is_up == False:
            turn_point_prices.append(last_turn_price)
            last_turn_price = close_prices[i]
    if close_prices[i] < last_turn_price:
        if revserse_direction_is_up == True:
            turn_point_prices.append(last_turn_price)
            last_turn_price = close_prices[i]

print(turn_point_prices)
print(len(turn_point_prices))


    

        