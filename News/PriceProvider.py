from os import listdir

import pandas as pd

from News import MinutePrices


class PriceProvider(object):

    root_path = 'C:/Users/david/Documents/Work/News/Research/minute/web/'
    suffix = ' intraday data.csv'

    def __init__(self):
        self.file_dates = set()

        for file in listdir(self.root_path):
            self.file_dates.add(file.split(' ')[0])

    def load_prices(self, date):  # YYYYMMDD format
        file_date = date[4:6] + '-' + date[6:8] + '-' + date[2:4]
        if self.file_dates.__contains__(file_date):
            filename = file_date + self.suffix
            df = pd.read_csv(self.root_path + filename)
            return MinutePrices.MinutePrice(df)


if __name__ == "__main__":
    pp = PriceProvider()
    mp = pp.load_prices('20151112')
    prices = mp.get_prices('IBM')
    df_sub = MinutePrices.get_window(prices, start='9:30', end='10:00')
    print(df_sub)
