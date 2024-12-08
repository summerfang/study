import pandas as pd
import yfinance as yf

import matplotlib.pyplot as plt

# Download the stock data from Yahoo Finance
# data = yf.download('FAS', start='2020-01-01', end='2023-01-01')

# Load the stock data
# Assuming the data is in a CSV file with columns: Date, Close
data = pd.read_csv('FAS.csv', parse_dates=['Date'], index_col='Date')

# Initialize buy and sell signals
data['Buy'] = pd.Series([None] * len(data), index=data.index)
data['Sell'] = pd.Series([None] * len(data), index=data.index)

# Iterate over the data to generate buy and sell signals
for i in range(2, len(data)):
    if data['Close'].iloc[i].item() > data['Close'].iloc[i-2].item():
        data.loc[data.index[i], 'Buy'] = data['Close'].iloc[i]
        stop_price = data['Close'].iloc[i-2].item()
        sell_found = False
        for j in range(i+1, len(data)):
            if data['Close'].iloc[j].item() < stop_price:
                data.loc[data.index[j], 'Sell'] = data['Close'].iloc[j]
                sell_found = True
                break
        if not sell_found:
            data.loc[data.index[i], 'Sell'] = None

# Plot the stock price and buy/sell signals
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.scatter(data.index, data['Buy'], label='Buy Signal', marker='^', color='green')
plt.scatter(data.index, data['Sell'], label='Sell Signal', marker='v', color='red')
plt.title('FAS Stock Buy and Sell Signals')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()


# Reset the index to have Date as a column
data.reset_index(inplace=True)

# Save the data to a CSV file
data.to_csv('FAS.csv', index=False)