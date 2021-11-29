from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from get_data import  get_data
import pandas as pd
import numpy as np

class calculate_support_resistance:
    def get_optimum_clusters(df, saturation_point=0.05):
        wcss = []
        k_models = []
        size = min(11, len(df.index))
        for i in range(1, size):
            kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=None)
            kmeans.fit(df)
            wcss.append(kmeans.inertia_)
            k_models.append(kmeans)

        #print(wcss)
        #print(k_models)

        #           SILOUETTE METHOD
        optimum_k = len(wcss) - 1
        for i in range(0, len(wcss) - 1):
            diff = abs(wcss[i + 1] - wcss[i])
            if diff < saturation_point:
                optimum_k = i
                break

        print("Optimum K is " + str(optimum_k + 1))
        optimum_clusters = k_models[optimum_k]

        return optimum_clusters

    def calculate(gran, ticker, start_date, end_date):
        csr = calculate_support_resistance
        gd = get_data

        lowss = []
        highss = []

        gd.feedData(gran, ticker, start_date, end_date)
        # print(time['granularity'])
        # print(time['timeframe'])
        df = pd.read_csv('data.csv', header=None)
        df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        # print(df)
        data = pd.DataFrame(df)
        data = data.set_index(pd.DatetimeIndex(data['Date']))
        # print(data)

        lows = pd.DataFrame(data=data, index=data.index, columns=["Low"])
        highs = pd.DataFrame(data=data, index=data.index, columns=["High"])

        low_clusters = csr.get_optimum_clusters(lows)
        low_centers = low_clusters.cluster_centers_
        low_centers = np.sort(low_centers, axis=0)

        high_clusters = csr.get_optimum_clusters(highs)
        high_centers = high_clusters.cluster_centers_
        high_centers = np.sort(high_centers, axis=0)

        for i in low_centers:
            # i = float(i)
            lowss.append(i)

        for i in high_centers:
            # i = float(i)
            highss.append(i)

        print('lows/support: ', lowss)
        print('highs/resistance: ', highss)

        return lowss, highss, data