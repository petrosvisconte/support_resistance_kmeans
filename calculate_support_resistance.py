from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

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

        # View inertia - good for electing the saturation point
        #print(wcss)

        # Compare differences in inertias until it's no more than saturation_point
        optimum_k = len(wcss) - 1
        for i in range(0, len(wcss) - 1):
            diff = abs(wcss[i + 1] - wcss[i])
            if diff < saturation_point:
                optimum_k = i
                break

        print("Optimum K is " + str(optimum_k + 1))
        optimum_clusters = k_models[optimum_k]

        return optimum_clusters