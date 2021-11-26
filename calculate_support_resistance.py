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
        optimum_clusters = k_models[9]


        #           ELBOW METHOD
        #from yellowbrick.cluster import KElbowVisualizer
        #model = KMeans()
        #visualizer = KElbowVisualizer(model, k=(2, 30), timings=True)
        #visualizer.fit(df)
        #print("Optimal K: ", str(visualizer.elbow_value_))
        #optimum_clusters = k_models[visualizer.elbow_value_]
        #visualizer.show()

        #           DENDOGRAM - HIERARCHICAL METHOD
        #import scipy.cluster.hierarchy as shc
        #from matplotlib import pyplot
        #pyplot.figure(figsize=(10, 7))
        #pyplot.title("Dendrograms")
        #dend = shc.dendrogram(shc.linkage(df, method='ward'))
        #pyplot.show()

        #           CALINSKI HARABASZ SCORE
        #from yellowbrick.cluster import KElbowVisualizer
        #model = KMeans()
        #visualizer = KElbowVisualizer(model, k=(2, 30), metric='calinski_harabasz', timings=True)
        #visualizer.fit(df)  # Fit the data to the visualizer
        #optimum_clusters = k_models[visualizer.elbow_value_]
        #visualizer.show()  # Finalize and render the figure

        return optimum_clusters