import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbols
tqqq_symbol = 'TQQQ'
sqqq_symbol = 'SQQQ'

# Download historical data
# tqqq_data = yf.download(tqqq_symbol, start='2000-01-02', end='2024-02-01')
# sqqq_data = yf.download(sqqq_symbol, start='2000-01-02', end='2024-02-01')

tqqq_data = yf.download(tqqq_symbol, start='2022-01-14', end='2024-02-01')
sqqq_data = yf.download(sqqq_symbol, start='2022-01-14', end='2024-02-01')

tqqq_data.to_csv('TQQQ_prices.csv', index=False)
sqqq_data.to_csv('SQQQ_prices.csv', index=False)

# Extract the 'Close' prices
tqqq_close = tqqq_data['Close']
sqqq_close = sqqq_data['Close']

# Calculate shares bought for TQQQ and SQQQ
initial_investment = 10000
tqqq_shares = initial_investment / tqqq_close.iloc[0]
sqqq_shares = initial_investment / sqqq_close.iloc[0]

# Calculate portfolio value
portfolio_value = tqqq_shares * tqqq_close + sqqq_shares * sqqq_close

# Plot the portfolio value over time
plt.figure(figsize=(10, 6))
plt.plot(portfolio_value.index, portfolio_value, label='Portfolio Value', color='b')
plt.xlabel('Date')
plt.ylabel('Portfolio Value ($)')
plt.title('TQQQ and SQQQ Portfolio Value')
plt.grid(True)
plt.legend()
plt.show()
plt.savefig('TQQQvsSQQQ.png')