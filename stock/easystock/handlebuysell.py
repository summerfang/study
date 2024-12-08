import pandas as pd

def handle_buy_sell(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Ensure the columns are named 'buy' and 'sell'
    if 'buy' not in df.columns or 'sell' not in df.columns:
        raise ValueError("CSV file must contain 'buy' and 'sell' columns")

    i = 0
    while i < len(df):
        # Find the next row with data in the 'buy' column
        while i < len(df) and pd.isna(df.at[i, 'buy']):
            i += 1
        if i >= len(df):
            break

        # Find the nearest row with data in the 'sell' column after the current 'buy' row
        j = i + 1
        while j < len(df) and pd.isna(df.at[j, 'sell']):
            j += 1
        if j >= len(df):
            break

        # Remove all 'sell' data between the current 'buy' row and the nearest 'sell' row
        df.loc[i+1:j, 'sell'] = None

        # Move the focus to the 'sell' column
        i = j

        # Clear all 'sell' data until the next row with data in the 'buy' column
        while i < len(df) and pd.isna(df.at[i, 'buy']):
            df.at[i, 'sell'] = None
            i += 1

    return df

# Example usage
file_path = '/c:/study/stock/easystock/FAS.csv'
result_df = handle_buy_sell(file_path)
result_df.to_csv('/c:/study/stock/easystock/processed_FAS.csv', index=False)