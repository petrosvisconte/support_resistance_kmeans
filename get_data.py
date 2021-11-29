import csv
import datetime
from oandapyV20.contrib.factories import InstrumentsCandlesFactory
from oandapyV20 import API

class get_data():
    def __init__(self):
        return

    def feedData(gran, ticker, start_date, end_date):
        #print("date and time:", date_time)
        # Oanda API setup
        # from oandapyV20 import API
        client = API(access_token='ecfc535793f6f636c305b190af8d86e2-4aaa4e49d92622062ecce655277c1749')
        instrument, granularity = ticker, gran
        stDt = start_date
        edDt = end_date
        #edDt = '2021-11-11T00:00:00Z'
        params = {'from': stDt, 'to': edDt, 'granularity': granularity}
        reList = []
        for r in InstrumentsCandlesFactory(instrument=instrument, params=params):
            client.request(r)
            reList = reList + r.response.get('candles')
        df = reList

        candles = reList
        # OHLC variables to return in array
        wO = []
        wH = []
        wL = []
        wC = []
        wV = []
        wD = []
        for x in range(0, len(reList)):
            candleData = candles[x].get("mid")
            candleDate = candles[x].get("time")
            v = candles[x].get("volume")
            o = candleData.get("o")
            h = candleData.get("h")
            l = candleData.get("l")
            c = candleData.get("c")
            wO.append(float(o))
            wH.append(float(h))
            wL.append(float(l))
            wC.append(float(c))
            wV.append(float(v))
            wD.append(candleDate)
        # Write to CSV
        with open("data.csv", "w") as csvfile:
            wr = csv.writer(csvfile, delimiter=',')
            for i in range(0, len(wO)):
                wr.writerow([wD[i], wO[i],wH[i],wL[i],wC[i],wV[i]])