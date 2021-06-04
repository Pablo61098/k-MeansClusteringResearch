import sklearn.cluster as cluster
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv("./dataFinal.csv")
data = data.iloc[:, 3:]
##############
# data = data.iloc[:, 2:14]
# data = data.iloc[:, 14:47]
# data = data.iloc[:, 47:55]
# data = data.iloc[:, 55:62]
# data = data.iloc[:, 62:67]
# data = data.iloc[:, 67:]
##############
# data = data.iloc[:, 3:15]
# data = data.iloc[:, 15:26]
# data = data.iloc[:, 26:34]
# data = data.iloc[:, 34:41]
# data = data.iloc[:, 41:]
print(data)

# ELBOW METHOD
K = range(1,8)
wss = []

for k in K:
    kmeans = cluster.KMeans(n_clusters=k, init="k-means++")
    kmeans = kmeans.fit(data)
    wss_iter = kmeans.inertia_
    wss.append(wss_iter)

plt.plot(K, wss, marker='o')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Within-cluster sum-of-squares criterion (WSS)')
plt.show()
