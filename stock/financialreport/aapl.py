import requests, json
# import yahoo_fin.stock_info as si
import yfinance as yf
from datetime import datetime
import pandas as pd

### Earnings functions
def _parse_earnings_json(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
):
        resp = requests.get(url, headers = headers)
        
        content = resp.content.decode(encoding='utf-8', errors='strict')
        
        page_data = [row for row in content.split(
            '\n') if row.startswith('root.App.main = ')][0][:-1]
        
        page_data = page_data.split('root.App.main = ', 1)[1]
        
        return json.loads(page_data)

def get_next_earnings_date(ticker):
        
    base_earnings_url = 'https://finance.yahoo.com/quote'
    new_url = base_earnings_url + "/" + ticker

    parsed_result = _parse_earnings_json(new_url)
    
    temp = parsed_result['context']['dispatcher']['stores']['QuoteSummaryStore']['calendarEvents']['earnings']['earningsDate'][0]['raw']

    return datetime.datetime.fromtimestamp(temp)

def get_earnings_history(ticker):
    
        '''Inputs: @ticker
           Returns the earnings calendar history of the input ticker with 
           EPS actual vs. expected data.'''

        url = 'https://finance.yahoo.com/calendar/earnings?symbol=' + ticker
         
        result = _parse_earnings_json(url)
        
        return result["context"]["dispatcher"]["stores"]["ScreenerResultsStore"]["results"]["rows"]

# Step 1: Get earnings history for a specific stock
# earnings_history = get_earnings_history("AAPL")  # Replace with your stock ticker

# Step 2: Fetch historical stock prices
ticker = yf.Ticker("NVDA")  # Replace with your stock ticker
historical_data = ticker.history(period="1y")

# Step 3: Calculate close price change before and after earnings date
# (You'll need to adjust this based on your data structure)
# Example: Calculate percentage change for the last earnings date
last_earnings_date = datetime.strptime('2023-08-23', "%Y-%m-%d")
before_earnings_close = historical_data.loc['2023-05-24']["Close"]
after_earnings_close = historical_data.loc['2023-05-25']["Close"]
percentage_change = ((after_earnings_close - before_earnings_close) / before_earnings_close) * 100

print(f"Percentage change for {last_earnings_date}: {percentage_change:.2f}%")

# Step 4: Repeat the process for the next earnings date
# next_earnings_date = si.get_next_earnings_date("AAPL")
next_earnings_date =  datetime.strptime('2024-02-21', "%Y-%m-%d")
# Calculate close price on the day before next earnings
# Calculate close price on next earnings date
# Compute percentage change

# Step 5: Identify the biggest gap in percentage change

# Your code here...
