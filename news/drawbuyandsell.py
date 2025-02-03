import pandas as pd

import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('FAS.csv')

plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.scatter(data.index, data['Buy'], label='Buy Signal', marker='^', color='green')
plt.scatter(data.index, data['Sell'], label='Sell Signal', marker='v', color='red')
plt.title('FAS Stock Buy and Sell Signals')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()