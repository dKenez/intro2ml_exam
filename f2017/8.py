def converge(s, clusters):
    K = len(clusters)

    averages = []

    for i in range(K):
        avg = 0
        for e in clusters[i]:
            avg += e

        avg /= len(clusters[i])

        averages.append(avg)

    return_clusters = []
    for i in range(K):
        return_clusters.append([])

    for e in s:
        min_d, min_i = -1, -1
        for i, avg in enumerate(averages):
            d = abs(avg-e)

            if i == 0 or d < min_d:
                min_d, min_i = d, i
        
        return_clusters[min_i].append(e)
    
    return return_clusters



o1 = 5.7
o2 = 6
o3 = 6.2
o4 = 6.3
o5 = 6.4
o6 = 6.6
o7 = 6.7
o8 = 6.9
o9 = 7
o10 = 7.4

s = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10]

k1 = [o1, o2, o3, o4, o5]
k2 = [o6, o7, o8, o9, o10]

clusters = [k1, k2]

for i in range(10):
    clusters = converge(s, clusters)

print(clusters)