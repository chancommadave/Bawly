import datetime as dt
import pandas as pd


class MinutePrice(object):
    symbol = 'Symbol'
    colon = ':'
    format = '%H:%M'

    def __init__(self, df):
        self.df = df

    def get_prices(self, symbol):
        prices = {}
        df = self.df
        df_symbol = df[df[self.symbol] == symbol]
        if df_symbol.empty:
            return
        raw_prices = df_symbol.to_dict()
        keys = df_symbol.to_dict().keys()
        for key in keys:
            if self.colon in key:
                substring = key[0:5]
                try:
                    t = dt.datetime.strptime(substring, self.format).time()
                    price = list(raw_prices[key].values())[0]
                    prices[t] = float(price)
                except ValueError:
                    print('Removed=' + key)
        return pd.Series(prices)


def get_window(series, start=None, end=None):
    new_series = series
    if start is not None:
        pd_start = dt.datetime.strptime(start, MinutePrice.format).time()
        new_series = new_series.loc[new_series.index >= pd_start]
    if end is not None:
        pd_end = dt.datetime.strptime(end, MinutePrice.format).time()
        new_series = new_series.loc[new_series.index < pd_end]
    return new_series