from calculate_support_resistance import calculate_support_resistance
from get_data import get_data
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import mplfinance as mpf
from get_date import get_date

gdate = get_date
date_last_week = gdate.return_date(7)
date_last_2week = gdate.return_date(14)
date_last_month = gdate.return_date(30)
date_last_3month = gdate.return_date(90)

time_frames = [
    {
        # 1 week 1 minute candles
        'timeframe': date_last_week,
        'granularity': 'M1'
    },
    {
        # 2 week 15 minute candles
       'timeframe': date_last_2week,
        'granularity': 'M15'
    },
    {
        # 1 month 1 hour candles
        'timeframe': date_last_month,
        'granularity': 'H1'
    },
    {
        # 3 months 4 hour candles
        'timeframe': date_last_3month,
        'granularity': 'H4'
    }

]

ticker_list = [
    {
        'ticker': 'USD_JPY',
        'rounding': 3
    },
    {
        'ticker': 'AUD_USD',
        'rounding': 5
    },
    {
        'ticker': 'EUR_USD',
        'rounding': 5
    },
    {
        'ticker': 'GBP_USD',
        'rounding': 4
    },
    {
        'ticker': 'NZD_USD',
        'rounding': 5
    },
    {
        'ticker': 'USD_CAD',
        'rounding': 5
    },
    {
        'ticker': 'USD_CHF',
        'rounding': 5
    },
    {
        'ticker': 'AUD_CAD',
        'rounding': 5
    },
    {
        'ticker': 'AUD_CHF',
        'rounding': 5
    },
    {
        'ticker': 'AUD_JPY',
        'rounding': 3
    },
    {
        'ticker': 'AUD_NZD',
        'rounding': 5
    },
    {
        'ticker': 'CAD_CHF',
        'rounding': 5
    },
    {
        'ticker': 'CAD_JPY',
        'rounding': 3
    },
    {
        'ticker': 'CHF_JPY',
        'rounding': 3
    },
    {
        'ticker': 'EUR_AUD',
        'rounding': 5
    },
    {
        'ticker': 'EUR_CAD',
        'rounding': 5
    },
    {
        'ticker': 'EUR_CHF',
        'rounding': 5
    },
    {
        'ticker': 'EUR_GBP',
        'rounding': 5
    },
    {
        'ticker': 'EUR_JPY',
        'rounding': 3
    },
    {
        'ticker': 'EUR_NZD',
        'rounding': 5
    },
    {
        'ticker': 'GBP_AUD',
        'rounding': 5
    },
    {
        'ticker': 'GBP_CAD',
        'rounding': 5
    },
    {
        'ticker': 'GBP_CHF',
        'rounding': 5
    },
    {
        'ticker': 'GBP_JPY',
        'rounding': 3
    },
    {
        'ticker': 'GBP_NZD',
        'rounding': 5
    },
    {
        'ticker': 'NZD_CAD',
        'rounding': 5
    },
    {
        'ticker': 'NZD_CHF',
        'rounding': 5
    },
    {
        'ticker': 'NZD_JPY',
        'rounding': 3
    },
    {
        'ticker': 'NZD_USD',
        'rounding': 5
    }
]


def main():
    for ticker in ticker_list:
        lowss = []
        highss = []
        finals = []
        for time in time_frames:
            csr = calculate_support_resistance
            gd = get_data

            gd.feedData(time['granularity'], ticker['ticker'], time['timeframe'])
            print(time['granularity'])
            print(time['timeframe'])
            df = pd.read_csv('data.csv', header=None)
            df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
            # print(df)
            data = pd.DataFrame(df)
            data = data.set_index(pd.DatetimeIndex(data['Date']))
            #print(data)

            lows = pd.DataFrame(data=data, index=data.index, columns=["Close"])
            highs = pd.DataFrame(data=data, index=data.index, columns=["High"])

            low_clusters = csr.get_optimum_clusters(lows)
            low_centers = low_clusters.cluster_centers_
            low_centers = np.sort(low_centers, axis=0)

            high_clusters = csr.get_optimum_clusters(highs)
            high_centers = high_clusters.cluster_centers_
            high_centers = np.sort(high_centers, axis=0)

            # How good are the clusters?
            #low_score = silhouette_score(lows, low_clusters.labels_)
            #high_score = silhouette_score(highs, high_clusters.labels_)
            #print(f"Silhouette score Lows: {low_score} Highs: {high_score}")

            rounding_factor = 2

            for i in low_centers:
                i = round(float(i), rounding_factor)
                lowss.append(i)

            for i in high_centers:
                i = round(float(i), rounding_factor)
                highss.append(i)

            print('lows/support: ', lowss)
            print('highs/resistance: ', highss)

            symbol = str(ticker['ticker'])
            # Plotting
            plt.style.use('fast')
            ohlc = data.loc[:, ['Open', 'High', 'Low', 'Close']]
            fig, ax = mpf.plot(ohlc.dropna(), type='candle', style='charles', show_nontrading=False, returnfig=True,
                           ylabel='Price', title=symbol)

            for low in low_centers[:9]:
                ax[0].axhline(low[0], color='green', ls='-', alpha=.2)

            for high in high_centers[-9:]:
                ax[0].axhline(high[0], color='red', ls='-', alpha=.1)

            plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
