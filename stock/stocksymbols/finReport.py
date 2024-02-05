import yahoo_fin.stock_info as si
import pandas as pd

symbol = "AAPL"  # Replace with the stock symbol you are interested in
earnings_history = si.get_earnings_history(symbol)

# Convert the earnings history to a Pandas DataFrame
df = pd.DataFrame(earnings_history)

# Save the data to a CSV file
df.to_csv("earnings_history.csv", index=False)
