# Q12: PCA to 2 components, plot clusters, report explained variance
# Also used for the segmentation task: K-Means on the reduced data.
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_wine(return_X_y=True)
X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print("Explained variance per component:", pca.explained_variance_ratio_.round(4))
print("Total explained variance:", round(pca.explained_variance_ratio_.sum(), 4))

# Segmentation: cluster the customers in PCA space
segments = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X_pca)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y)
ax[0].set_title("PCA - true classes")
ax[1].scatter(X_pca[:, 0], X_pca[:, 1], c=segments)
ax[1].set_title("PCA - K-Means segments")
plt.savefig("pca_clusters.png")
