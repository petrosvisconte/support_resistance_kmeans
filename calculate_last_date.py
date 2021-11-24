import DateTime.DateTime

from get_data import get_data
from get_date import get_date
import pandas as pd

class calculate_last_date:
    def get_data(ticker):
        gd = get_data
        gdate = get_date

        date_last_10year = gdate.return_date(3600)
        gd.feedData('D', ticker, date_last_10year)

        df = pd.read_csv('data.csv', header=None)
        df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        data = pd.DataFrame(df)

        return data

    def get_last_date(ticker):
        cld = calculate_last_date
        data = cld.get_data(ticker)

        last_low_price = 0
        last_low_date = ''

        for i in range(len(data)):
            high = float(data.loc[i, 'High'])
            date = data.loc[i, 'Date']
            latest_price = float(data.tail(1).get('Close'))
            #print(latest_price)
            #print(high / latest_price)
            if high / latest_price <= 0.96:
                last_low_price = high
                last_low_date = date
                #print(date)
        #print(last_low_price)
        #print(last_low_date)
        last_low = [last_low_date, last_low_price]

        return last_low