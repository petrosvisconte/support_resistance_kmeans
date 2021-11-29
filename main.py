import datetime
from calculate_support_resistance import calculate_support_resistance
from get_date import get_date
from calculate_last_date import calculate_last_date
from dateutil import parser
from plot_data import plot_data

begin_time = datetime.datetime.now()

now = datetime.datetime.utcnow()
date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")

gdate = get_date
date_last_week = gdate.return_date(7)
date_last_2week = gdate.return_date(14)
date_last_month = gdate.return_date(30)
date_last_3month = gdate.return_date(90)

time_frames = [
    {
        # 1 week 1 minute candles
        'timeframe': date_last_week,
        'granularity': 'M1',
        'end_date': date_time
    },
    {
        # 2 week 5 minute candles
       'timeframe': date_last_2week,
        'granularity': 'M5',
        'end_date': date_time
    },
    {
        # 1 month 15 minute candles
        'timeframe': date_last_month,
        'granularity': 'M15',
        'end_date': date_time
    },
    {
        # 3 months 1 hour candles
        'timeframe': date_last_3month,
        'granularity': 'H1',
        'end_date': date_time
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

        cld = calculate_last_date
        last = cld.get_last_date(ticker['ticker'], date_time)

        last = last[0]
        last = last[:11]
        last = parser.parse(last)
        # print(last)

        first = datetime.datetime.utcnow()
        first = str(first)
        first = first[:11]
        first = parser.parse(first)
        # print(first)

        delta = first - last
        print(delta.days)

        end_date = str(cld.get_forward_date(ticker['ticker'], date_time))
        end_date = end_date[:16] + ':00Z'
        print(end_date)

        time_frames.append({'timeframe': gdate.return_date(delta.days), 'granularity': 'M15', 'end_date': end_date})
        time_frames.append({'timeframe': gdate.return_date(delta.days), 'granularity': 'H1', 'end_date': date_time})

        for time in time_frames:
            csr = calculate_support_resistance
            lowss, highss, data = csr.calculate(time['granularity'], ticker['ticker'], time['timeframe'], time['end_date'])

        time_frames.pop(5)
        time_frames.pop(4)

        plotd = plot_data
        plotd.plot(ticker['ticker'], data, lowss, highss)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
