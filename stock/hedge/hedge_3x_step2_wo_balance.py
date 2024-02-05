import os
import pandas as pd
from hedge_3x_step1_stock_ohlc_csv import download_price_symbol
import matplotlib.pyplot as plt
import numpy as np

def plot_stock_curve(start_date, end_date, symbol):
    # Read the OHLC data from the file
    file_path = os.path.join(os.path.dirname(__file__), 'stocks', f'{symbol}.csv')

    if not os.path.exists(file_path):
        download_price_symbol(symbol, start_date, end_date)
    df = pd.read_csv(file_path)

    # Filter the data based on the start and end dates
    df['Date'] = pd.to_datetime(df['Date'])
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    filtered_df = df.loc[mask]

    # Plot the curve based on the close prices
    plt.plot(filtered_df['Date'], filtered_df['Close'])
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'Stock Curve for {symbol}')
    plt.show()

def plot_hedge_stocks_curves(start_date, end_date, hedge_symbols_pair=('SOXL', 'SOXS')):
    plt.figure()  # Create a new figure
    
    for symbol in hedge_symbols_pair:

        file_path = os.path.join(os.path.dirname(__file__), 'stocks', f'{symbol}.csv')

        if not os.path.exists(file_path):
            download_price_symbol(symbol, start_date, end_date)
        df = pd.read_csv(file_path)

        # Filter the data based on the start and end dates
        df['Date'] = pd.to_datetime(df['Date'])
        mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        filtered_df = df.loc[mask]
        plt.plot(filtered_df['Date'], filtered_df['Close'])

    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Stock Curves')
    plt.legend(hedge_symbols_pair)  # Add a legend with the symbols
    plt.show()


def hedge_3x_stocks(start_date, end_date, symbols, initial_investment=10000) -> float:
    # Calculate the daily end value for each symbol
    daily_end_values = []
    for symbol in symbols:
        file_path = os.path.join(os.path.dirname(__file__), 'stocks', f'{symbol}.csv')

        if not os.path.exists(file_path):
            download_price_symbol(symbol, start_date, end_date)
        df = pd.read_csv(file_path)

        # Filter the data based on the start and end dates
        df['Date'] = pd.to_datetime(df['Date'])
        mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        filtered_df = df.loc[mask]

        # Calculate the daily end value based on the close prices
        daily_end_value = filtered_df['Close'] * (initial_investment / filtered_df['Close'].iloc[0])
        daily_end_values.append(daily_end_value)

    # Calculate the portfolio value as the sum of the daily end values
    portfolio_value = sum(daily_end_values)
    last_value = portfolio_value.iloc[-1]
    # Calculate the profit
    profit = last_value - (initial_investment * len(symbols))

    profit_percentage = (profit / (initial_investment * len(symbols))) * 100
    
    return profit_percentage

def plot_hedge_3x_stocks_curves(start_date, end_date, symbols: tuple = ('SOXL', 'SOXS'), initial_investment=10000):
    # Calculate the daily end value for each symbol
    daily_end_values = []
    for symbol in symbols:
        file_path = os.path.join(os.path.dirname(__file__), 'stocks', f'{symbol}.csv')

        if not os.path.exists(file_path):
            download_price_symbol(symbol, start_date, end_date)
        df = pd.read_csv(file_path)

        # Filter the data based on the start and end dates
        df['Date'] = pd.to_datetime(df['Date'])
        mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        filtered_df = df.loc[mask]

        # Calculate the daily end value based on the close prices
        daily_end_value = filtered_df['Close'] * (initial_investment / filtered_df['Close'].iloc[0])
        daily_end_values.append(daily_end_value)
        daily_close_prices = filtered_df['Close']
        daily_end_values.append(daily_close_prices)

    # Calculate the portfolio value as the sum of the daily end values
    portfolio_value = daily_end_values[0] + daily_end_values[2]
    last_value = portfolio_value.iloc[-1]
    # Calculate the profit
    profit = last_value - (initial_investment * len(symbols))

    profit_percentage = (profit / (initial_investment * len(symbols))) * 100
   
    fig, ax = plt.subplots()
    
    ax2 = ax.twinx()

    # Plot the curves
    if np.mean(daily_end_values[0]) > np.mean(daily_end_values[1]):
        ax.plot(filtered_df['Date'], daily_end_values[0], color = 'red', label=f'{symbols[0]} value')
        ax.plot(filtered_df['Date'], daily_end_values[2], color = 'green', label=f'{symbols[1]} value')
        ax2.plot(filtered_df['Date'], daily_end_values[1], color = 'pink', label=f'Daily Price: {symbols[0]}')
        ax2.plot(filtered_df['Date'], daily_end_values[3], color = 'lightgreen', label=f'Daily Price: {symbols[1]}')

    else:
        ax.plot(filtered_df['Date'], daily_end_values[0], color = 'green', label=f'{symbols[0]} value')
        ax.plot(filtered_df['Date'], daily_end_values[2], color = 'red', label=f'{symbols[1]} value')
        ax2.plot(filtered_df['Date'], daily_end_values[1], color = 'lightgreen', label=f'Daily Price: {symbols[0]}')
        ax2.plot(filtered_df['Date'], daily_end_values[3], color = 'pink', label=f'Daily Price: {symbols[1]}')

    ax.plot(filtered_df['Date'], portfolio_value, color = 'k', label='Portfolio')
    # ax.xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_title(f'Start from {start_date} to {end_date}\nProfit: {profit_percentage:.2f}%')
    ax.legend(loc = 'center left')

    ax2.set_ylabel('Daily Price')
    ax2.legend(loc='center right')

    plt.xticks(rotation=45)
    plt.show()


def plot_3xhedge_stocks_curves_in1figure(start_date, end_date, symbols, initial_investment, ax):
    # Calculate the daily end value for each symbol
    daily_end_values = []
    for symbol in symbols:
        file_path = os.path.join(os.path.dirname(__file__), 'stocks', f'{symbol}.csv')

        if not os.path.exists(file_path):
            download_price_symbol(symbol, start_date, end_date)
        df = pd.read_csv(file_path)

        # Filter the data based on the start and end dates
        df['Date'] = pd.to_datetime(df['Date'])
        mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        filtered_df = df.loc[mask]

        # Calculate the daily end value based on the close prices
        daily_end_value = filtered_df['Close'] * (initial_investment / filtered_df['Close'].iloc[0])
        daily_end_values.append(daily_end_value)

    # Calculate the portfolio value as the sum of the daily end values
    portfolio_value = sum(daily_end_values)
    last_value = portfolio_value.iloc[-1]
    # Calculate the profit
    profit = last_value - (initial_investment * len(symbols))

    profit_percentage = (profit / (initial_investment * len(symbols))) * 100

    # Plot the curves
    ax.plot(filtered_df['Date'], daily_end_values[0], label=f'{symbols[0]}')
    ax.plot(filtered_df['Date'], daily_end_values[1], label=f'{symbols[1]}')
    ax.plot(filtered_df['Date'], portfolio_value, label='Portfolio')
    # ax.xlabel('Date')
    # ax.ylabel('Value')
    # ax.title(f'Start from {start_date} to {end_date}\nProfit: {profit_percentage:.2f}%')
    # ax.legend()

if __name__ == "__main__":
    plot_hedge_3x_stocks_curves('2020-01-01', '2020-12-31', ('SOXL','SOXS'))