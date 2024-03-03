import yfinance as yf

ticker_stock = 'UVXY'

# Create a Ticker object for the stock (e.g., AAPL for Apple)
stock_symbol = yf.Ticker(ticker_stock)

# Get historical data (including closing prices)
historical_data = stock_symbol.history(period="1d")
last_close_price = historical_data["Close"].iloc[-1]

print(f"Last close price for {ticker_stock}: ${last_close_price:.2f}")


print(f'{"date":^20}{"strike price":^30}{"percentage2profit":^30}{"percentage2cost":^30}{"vs ratio":^30}')
# Get option chain data
for j in range(0, 5):
    date_str = stock_symbol.options[j]

    df_options = stock_symbol.option_chain(stock_symbol.options[j])
    # print(df_options.calls[df_options.calls['strike']>float(last_close_price)])

    # percentage = 0
    for i in range(1):
        strike_price = df_options.calls[df_options.calls['strike']>float(last_close_price)].iloc[i]['strike']
        last_price_of_option = df_options.calls[df_options.calls['strike']>float(last_close_price)].iloc[i]['lastPrice']
        percentage2profit = (strike_price + last_price_of_option - last_close_price)/last_close_price
        percentage2cost = last_price_of_option/last_close_price
        print(f'{date_str:^20}{strike_price:^30}{percentage2profit:^30.2%}{percentage2cost:^30.2%}{percentage2cost/percentage2profit:^30.2%}')