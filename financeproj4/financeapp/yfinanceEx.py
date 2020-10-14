from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf

startDate = '2012-01-01'
endDate = str(datetime.now().strftime('%Y-%m-%d'))
print('endDate=', endDate)

# ticker
usaStock = 'AMZN'

# Retrieves stats - step 3


def get_stats(stock_data):
    return {
        'last': np.mean(stock_data.tail(1)),
        'short_mean': np.mean(stock_data.tail(20)),
        'long_mean': np.mean(stock_data.tail(20)),
        'short_rolling': stock_data.rolling(window=20).mean(),
        'long_rolling': stock_data.rolling(window=200).mean()
    }

# Cleans the data - step 2


def clean_data(stock_data, col):
    weekdays = pd.date_range(start=startDate, end=endDate)
    clean_data = stock_data[col].reindex(weekdays)
    # ffill handles all non number values
    return clean_data.fillna(method='ffill')


# Creates the plot - step 4


def create_plot(stock_data, ticker):
    stats = get_stats(stock_data)
    plt.subplots(figsize=(12, 8))
    plt.plot(stock_data, label=ticker)
    plt.plot(stats['short_rolling'], label='200 day rolling mean')
    plt.plot(stats['long_rolling'], label='200 day rolling mean')
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close ($)')
    plt.legend()
    plt.title('Stock Price over Time')
    plt.show()

# Gets the data - step 1


def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker, 'yahoo', startDate, endDate)
        adj_close = clean_data(stock_data, 'Adj Close')
        create_plot(adj_close, ticker)

    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))


get_data(usaStock)
