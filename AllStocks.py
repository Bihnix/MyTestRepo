import pandas as pd
import numpy as np
import yfinance as yf
import os
import matplotlib.pyplot as plt

"""
This script fetches historical stock prices for a list of FAANG companies (Apple, Amazon, Meta, Google, and Netflix)
from Yahoo Finance using the yfinance library. It calculates daily, monthly, and weekly returns for each company.
The data is then saved as CSV files and plotted as separate subplots for each company.
"""

# Define the FAANG company symbols
symbols = ['AAPL', 'AMZN', 'meta', 'GOOGL', 'NFLX']

# Define the start and end dates for the historical data
start_date = '2000-01-01'
end_date = '2024-04-30'

def getPrice(stockName,start_date, end_date):
    """
    Fetches historical stock prices for a given symbol from Yahoo Finance.

    Parameters:
    stockName (str): The symbol of the stock.
    start_date (str): The start date of the historical data in 'YYYY-MM-DD' format.
    end_date (str): The end date of the historical data in 'YYYY-MM-DD' format.

    Returns:
    pandas.DataFrame: A DataFrame containing the historical stock prices.
    """
    data = yf.download(tickers= stockName, start=start_date, end=end_date)
    return data


def calculate_returns(data):
    """
    Calculates daily, monthly, and weekly returns for a given DataFrame of stock prices.

    Parameters:
    data (pandas.DataFrame): A DataFrame containing the historical stock prices.

    Returns:
    pandas.DataFrame: The input DataFrame with additional columns for daily, monthly, and weekly returns.
    """
    data['Daily_Return'] = data['Close'].pct_change()
    #addin montghly return
    data['Monthly_Return'] = data['Close'].pct_change(30)
    #adding weekly return
    data['Weekly_Return'] = data['Close'].pct_change(7)
    return data

if not os.path.exists('/Users/behnamebrahimi/Developer/MyTestRepo/Export'):
    os.makedirs('/Users/behnamebrahimi/Developer/MyTestRepo/Export')
        
# Fetch the historical prices for each symbol
for symbol in symbols:
    prices = getPrice(symbol, start_date, end_date)
    calculate_returns(prices)
    # Create a CSV file for each stock
    folder_name = 'Export'
    filename = f"{symbol}_historical_data.csv"
    # Create the directory if it does not exist

    file_path = f"/Users/behnamebrahimi/Developer/MyTestRepo/{folder_name}/{filename}"
    prices.to_csv(file_path)

    print(f"Saved {symbol} historical data to {filename}")

 
# plot the daily returns for each stock in separate subplots
fig, axs = plt.subplots(len(symbols), 1, figsize=(10, 8), sharex=True)

for i, symbol in enumerate(symbols):
    # Read the CSV file for each stock
    file_path = f"/Users/behnamebrahimi/Developer/MyTestRepo/{folder_name}/{filename}"
    prices = pd.read_csv(file_path)
    
    # Create a new figure and subplot for each stock
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Plot the daily returns
    ax.plot(prices.index, prices['Daily_Return'])
    ax.set_title(f"{symbol} Daily Returns")
    ax.set_xlabel('Date')
    ax.set_ylabel('Return')
    
    # Save the figure as an image
    fig.savefig(f"/Users/behnamebrahimi/Developer/MyTestRepo/{folder_name}/{symbol}_daily_returns.png")
    
    # Close the figure to free up memory
    plt.close(fig)
    
    # Create a new figure and subplot for each stock
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Plot the monthly returns
    ax.plot(prices.index, prices['Monthly_Return'])
    ax.set_title(f"{symbol} Monthly Returns")
    ax.set_xlabel('Date')
    ax.set_ylabel('Return')
    
    # Save the figure as an image
    fig.savefig(f"/Users/behnamebrahimi/Developer/MyTestRepo/{folder_name}/{symbol}_monthly_returns.png")
    
    # Close the figure to free up memory
    plt.close(fig)
    
    # Create a new figure and subplot for each stock
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Plot the weekly returns
    ax.plot(prices.index, prices['Weekly_Return'])
    ax.set_title(f"{symbol} Weekly Returns")
    ax.set_xlabel('Date')
    ax.set_ylabel('Return')
    
    # Save the figure as an image
    fig.savefig(f"/Users/behnamebrahimi/Developer/MyTestRepo/{folder_name}/{symbol}_weekly_returns.png")
    
    # Close the figure to free up memory
    plt.close(fig)
    
    print(f"Saved {symbol} returns charts")
    
plt.tight_layout()
plt.show()