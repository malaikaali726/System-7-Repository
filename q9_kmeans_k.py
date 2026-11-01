# Q9: K-Means for k = 2..10, elbow curve and silhouette scores
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

ks = list(range(2, 11))
inertias, silhouettes = [], []
for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X, km.labels_))

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(ks, inertias, "o-")
ax[0].set_title("Elbow curve")
ax[0].set_xlabel("k")
ax[0].set_ylabel("Inertia")
ax[1].plot(ks, silhouettes, "o-")
ax[1].set_title("Silhouette score")
ax[1].set_xlabel("k")
plt.savefig("kmeans_k_selection.png")

best_k = ks[silhouettes.index(max(silhouettes))]
print("Best k by silhouette:", best_k)
