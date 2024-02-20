from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import yfinance as yf
from download_symbol_price_history import download_price_symbol
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def get_stock_fin_rpt_days(ticker):
    url = 'https://finance.yahoo.com/calendar/earnings?symbol=' + ticker
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    resp = requests.get(url, headers = headers)
        
    html_content = resp.content.decode(encoding='utf-8', errors='strict')

    # html_content = "<your HTML content here>"
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the first table with class="W(100%)"
    table = soup.find('table', class_='W(100%)')

    tbody = table.find_all('tbody')
    rows = tbody[0].find_all('tr') 

    stock_financial_report_days = []

    for row in rows:
        cols = row.find_all('td')
        spans = cols[2].find_all('span')
        date_str_wo_tz = spans[0].text
        date_str_tz = spans[1].text
        format_string = f"%b %d, %Y, %I %p"
        dt = datetime.strptime(date_str_wo_tz, format_string)

        if date_str_tz in {'EDT', 'EST'}:
            date_before_rpt = dt.strftime("%Y-%m-%d")
            offset = pd.tseries.offsets.BusinessDay(n=1)
            one_day_after = dt + offset

            date_after_rpt = one_day_after.strftime("%Y-%m-%d")
            next_qrpt_date = (dt + timedelta(days=90)).strftime("%Y-%m-%d")

            if date_after_rpt < datetime.now().strftime("%Y-%m-%d"):
                print(f'{date_before_rpt} {date_after_rpt} {next_qrpt_date}')
                stock_financial_report_days.append((date_before_rpt, date_after_rpt, next_qrpt_date))
        else:
            offset = pd.tseries.offsets.BusinessDay(n=1)
            one_date_before = dt - offset
            date_before_rpt = one_date_before.strftime("%Y-%m-%d")
            date_after_rpt = dt.strftime("%Y-%m-%d")
            next_qrpt_date = (dt + timedelta(days=89)).strftime("%Y-%m-%d")

            if date_after_rpt < datetime.now().strftime("%Y-%m-%d"):
                print(f'{date_before_rpt} {date_after_rpt} {next_qrpt_date}')
                stock_financial_report_days.append((date_before_rpt, date_after_rpt, next_qrpt_date))

    return stock_financial_report_days

def get_price_change_list_after_qrpt(ticker, start_date='2000-01-01', end_date='2024-02-01)'):
    days = get_stock_fin_rpt_days(ticker)


    historical_data = download_price_symbol(ticker, start_date, end_date)

    price_list = []

    for day in days:
        try:
            before_earnings_close = historical_data.loc[day[0]]["Close"]
            after_earnings_close = historical_data.loc[day[1]]["Close"]
            percentage_change = ((after_earnings_close - before_earnings_close) / before_earnings_close) * 100
            price_list.append((day[0], percentage_change))
        except KeyError:
            print(f'Error: {day[0]}, skipping...')       

    return price_list

def get_success_ratio(ticker, current_price, low_break_even_price, high_break_even_price):
    low_percentage = (low_break_even_price - current_price) * 100 / current_price
    high_percentage = (high_break_even_price - current_price) * 100 / current_price

    prices = get_price_change_list_after_qrpt(ticker, start_date='2000-01-01', end_date='2023-12-01')

    prices_list = [p[1] for p in prices]
    price_series = pd.Series(prices_list)
    summary = price_series.describe()

    low_z_score = (low_percentage - summary['mean']) / summary['std']
    low_p = stats.norm.cdf(low_z_score)

    high_z_score = (high_percentage - summary['mean']) / summary['std']
    high_p = 1 - stats.norm.cdf(high_z_score)

    success_ratio = (low_p + high_p) * 100

    return success_ratio, [summary['mean'], summary['std'], low_z_score, high_z_score]




def draw_normal_distribution(mean, std_dev, low_z_score, high_z_score):
    # Create an array of values for the x-axis (from mean - 3*std_dev to mean + 3*std_dev)
    x_values = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 1000)

    # Calculate the normal distribution (PDF) using scipy's norm.pdf
    pdf_values = norm.pdf(x_values, mean, std_dev)

    # Plot the normal distribution
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, pdf_values, label="Normal Distribution", color="blue")
    plt.title("Normal Distribution")
    plt.xlabel("X")
    plt.ylabel("Probability Density")
    plt.grid(True)
    plt.legend()

    # Calculate z-scores for specific percentiles
    low_percentile = norm.cdf(low_z_score, mean, std_dev)
    high_percentile = norm.cdf(high_z_score, mean, std_dev)

    print(f"Low Z-Score (5% percentile): {low_z_score:.2f} (Probability: {low_percentile:.2f})")
    print(f"High Z-Score (95% percentile): {high_z_score:.2f} (Probability: {high_percentile:.2f})")

    # Show the plot
    plt.show()

success_ratio, distribution = get_success_ratio('WMT', 170.36, 162.36, 180.14)
print(f'{success_ratio:.2f}%')

draw_normal_distribution(distribution[0], distribution[1], distribution[2], distribution[3])

