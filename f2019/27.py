import numpy as np

x = np.array([0.4, 0.5, 1.1, 2.2, 2.6, 3.0, 3.6, 3.7, 4.9, 5.0])

clust_cent = np.array([2.4, 3.3, 3.5])

def converge(x, clust_cent):
    clusters = []

    for _ in clust_cent:
        clusters.append([])

    for e in x:
        min_i, min_d = -1, -1
        for i, j in enumerate(clust_cent):
            d = abs(e - j)
            if i == 0 or d < min_d:
                min_i, min_d = i, d
        
        clusters[min_i].append(e)

    for i, cluster in enumerate(clusters):
        clust_cent[i] = np.mean(cluster)

    return clusters, clust_cent

for i in range(10):
    clusters, clust_cent = converge(x, clust_cent)

print(clusters)