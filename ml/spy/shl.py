def find_breakout_points(prices):
    breakout_points = []
    trend = None
    prev_price = None
    prev_index = None

    for i, price in enumerate(prices):
        if prev_price is not None:
            if trend == 'up':
                if price < prev_price:
                    if price < min(prices[prev_index:i]):
                        breakout_points.append((i, price))
                        trend = 'down'
            elif trend == 'down':
                if price > prev_price:
                    if price > max(prices[prev_index:i]):
                        breakout_points.append((i, price))
                        trend = 'up'
            else:
                if price > prev_price:
                    trend = 'up'
                elif price < prev_price:
                    trend = 'down'

        prev_price = price
        prev_index = i

    return breakout_points

# Read the stock price data from the file
data = []
with open('SPY_30min_sample.txt', 'r') as file:
    for line in file:
        timestamp, a, b, c, price, d = line.strip().split(',')
        data.append((timestamp, float(price)))

# Extract the prices from the data
prices = [price for _, price in data]

# Example usage:
# prices = [10, 12, 8, 15, 13, 20, 18, 25, 22, 30]
breakout_points = find_breakout_points(prices)
print(breakout_points)
