import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csv_file = 'CountyCrossWalk_Zillow.csv'

df = pd.read_csv(csv_file)

plt.plot(df.StateName, df.CountyFIPS, 'o', color='black')

plt.show()