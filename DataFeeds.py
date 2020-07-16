from polygon import RESTClient
import alpaca_trade_api as tradeapi
import pandas as pd
from datetime import datetime
import requests
import pytz
import config

key = config.Polycon['key']
client = RESTClient(key)

alpacaKey = config.Alpaca['key']
secret = config.Alpaca['secret']
base_url = config.Alpaca['base_url']
api = tradeapi.REST(alpacaKey, secret, base_url, api_version='v2')


def MarketGroup(inputDate):
    '''
    Gives most recent snapshot of all Stock Prices.
    Returns around 8k Results

    Example MarketGroup('AAPL', '2020-07-14')

    '''
    data = client.stocks_equities_grouped_daily(
        locale='US', market='STOCKS', date=inputDate)
    df = pd.DataFrame(data.results)
    df['change'] = (df['c'] / df['o']) - 1.0000
    # df = df[df['change'] >= 0.10]
    return df


def HistoricTrades(symbol, inputDate):
    '''
    Gives historic trades by Nanosecond accuracy.
    Limits by only 50k results

    Example HistoricTrades('AAPL', '2020-07-14')

    '''
    data = client.historic_trades_v2(symbol, inputDate)
    df = pd.DataFrame(data.results)
    # TimeStamps are in UNIX nanoseconds
    df['dateTime'] = pd.to_datetime(df['t'], unit='ns')
    return df


def HistoricPrices1Min(symbol, startDate, endDate):

    url = 'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/minute/{startDate}/{endDate}?sort=asc&apiKey={apiKey}'.format(
        symbol=symbol, startDate=startDate, endDate=endDate, apiKey=key)
    data = requests.get(url).json()
    data_df = pd.DataFrame.from_dict(data['results'])

    data_df['timestamp'] = data_df['t'].astype('datetime64[ms]')
    data_df = data_df.set_index('timestamp')

    # Timestamp is in UTC - Converting Time to US/Eastern
    # https://stackoverflow.com/questions/22800079/converting-time-zone-pandas-dataframe
    eastern = pytz.timezone('US/Eastern')
    data_df.index = data_df.index.tz_localize(pytz.utc).tz_convert(eastern)

    # Time for Only When Market is open
    # To match Charts prices -  use following - For end date use 16:00 Open; For start use 9:30 Close
    data_df = data_df.between_time('09:30', '16:00')
    print(data_df.sort_values(by=['t'], ascending=False))

    #print(HistoricTrades('AAPL', '2020-07-14'))
    #HistoricPrices1Min('XOM', '2005-07-14', '2020-07-16')


def AlpacaHistoric(symbol, startDate, endDate, timeFrame='1Min'):
    # https://github.com/alpacahq/alpaca-trade-api-python/issues/109
    data = (api.get_barset(symbols=[symbol], timeframe=timeFrame, start=pd.Timestamp(
        startDate, tz='America/New_York').isoformat(), end=pd.Timestamp(endDate, tz='America/New_York').isoformat())).df
    #data = data.between_time('09:30', '16:00')
    print(data)
    # data.to_csv('test.csv')


if __name__ == '__main__':
    print('TESTING')
    #AlpacaHistoric('TSLA', '2020-07-14', '2020-07-15')
    HistoricPrices1Min('TSLA', '2020-07-15', '2020-07-15')
