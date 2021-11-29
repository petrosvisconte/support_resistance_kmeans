import mplfinance as mpf
from matplotlib import pyplot as plt

class plot_data:
    def plot(ticker, data, lowss, highss):
        symbol = str(ticker)
        # Plotting
        plt.style.use('fast')
        ohlcv = data.loc[:, ['Open', 'High', 'Low', 'Close', 'Volume']]
        ohlcv = ohlcv.tail(1000)
        fig, ax = mpf.plot(ohlcv.dropna(), type='candle', style='charles', show_nontrading=False, returnfig=True,
                           ylabel='Price', title=symbol, volume=True)

        current_price = float(data.tail(1).get('Close'))
        for low in lowss:
            if low > current_price:
                ax[0].axhline(low[0], color='red', ls='-', alpha=.2)
            else:
                ax[0].axhline(low[0], color='green', ls='-', alpha=.2)

        #for high in highss:
        #    if high > current_price:
        #        ax[0].axhline(high[0], color='red', ls='-', alpha=.1)
        #    else:
        #        ax[0].axhline(high[0], color='green', ls='-', alpha=.2)
        plt.show()