#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
sns.set()

#Def to get data
def get_polygons(url):
    pol = pd.read_csv(url)
    print("Your file had been processed:", pol.head(5))
    return(pol)

def cluster_polygons (polygons, k):
    # Weighted clusters by freq. per neighbor
    polygons_cl = polygons
    kmeans = KMeans(n_clusters=9, max_iter=1000, init='k-means++')
    lat_long = polygons_cl[polygons_cl.columns[1:3]]
    count = polygons_cl[polygons_cl.columns[4]]
    weighted_kmeans_clusters = kmeans.fit(lat_long, sample_weight = count)  # Compute k-means clustering.
    centers = kmeans.cluster_centers_  # Coordinates of cluster centers.
    polygons_cl['cluster_label'] = kmeans.predict(lat_long, sample_weight = count)
    print("Your input had been clustered:", polygons_cl.head(3))
    print("Your clusters looks like this:")
    labels = polygons_cl['cluster_label']  # Labels of each point
    polygons_cl.plot.scatter(x='Centroid Lat', y='Centroid Lon', c=labels, s=50, cmap='twilight')
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=100, alpha=0.3),
    plt.xlabel("Latitude"),
    plt.ylabel("Longitude")
    plt.show()
    return (polygons_cl)

url = "/Users/adrsanchez/PycharmProjects/Mobility-in-Mexico-City/datasets/cluster_input.csv"
k= 10
polygons = get_polygons(url)
cluster_polygons(polygons, k)


