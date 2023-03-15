import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

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

df_spy_min = pd.read_csv('SPY_1min_sample.txt', sep=',', header=None)
df_spy_min.columns = ['Date Time', 'open', 'high', 'low', 'close', 'volume']

print(get_wave_point(df_spy_min, 'close'))


    

        