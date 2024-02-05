import yfinance as yf
import os
import os.path as file
import pandas as pd
from datetime import datetime, timedelta

def download_price_symbol(symbol, start_date, end_date):
    current_directory = os.path.dirname(os.path.abspath(__file__))

    stocks_directory = os.path.join(current_directory, 'stocks')
    if not file.exists(stocks_directory):
        os.makedirs(stocks_directory)

    stocks_file_full_path = os.path.join(stocks_directory, f'{symbol}.csv')
    if not file.exists(stocks_file_full_path):
        data = yf.download(symbol, start=start_date, end=end_date)
        file_path = os.path.join(stocks_directory, f'{symbol}.csv')
        data.reset_index(inplace=True)  # Reset index to include date as a separate column
        data.to_csv(file_path, index=False)
    else:
        data = pd.read_csv(stocks_file_full_path)
        last_date = data['Date'].iloc[-1]
        if last_date < end_date:
            last_date = datetime.strptime(last_date, "%Y-%m-%d")
            new_start_date = (last_date + timedelta(days=1)).strftime("%Y-%m-%d")
            new_data = yf.download(symbol, start=new_start_date, end=end_date)
            new_data.reset_index(inplace=True)
            data = pd.concat([data, new_data])
            data.drop_duplicates(subset='Date', keep='first', inplace=True)
            data.to_csv(stocks_file_full_path, index=False)

if __name__ == "__main__":
    symbols = ['TQQQ', 'SQQQ', 
               'SOXL', 'SOXS', 
               'YINN', 'YANG', 
               'BOIL', 'KOLD', 
               'DRN', 'DRV', 
               'LABU', 'LABD', 
               'UPRO', 'SPXU', 
               'TECL', 'TECS', 
               'DRIP', 'GUSH', 
               'TSA', 'TNA', 
               'FAS', 'FAZ', 
               'UDOW', 'SDOW', 
               'FNGU', 'FNGD', 
               'NRGU', 'NRGD', 
               'OILU', 'OILD']

    for symbol in symbols:
        download_price_symbol(symbol, '2000-01-01', '2024-2-1')


