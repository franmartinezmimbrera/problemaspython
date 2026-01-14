from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generar datos sintéticos (nubes de puntos)
X, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.60, random_state=0)

# Configurar K-Means para buscar 3 grupos (clusters)
kmeans = KMeans(n_clusters=3, n_init=10)
# Ajustar el modelo (aquí no hay 'y' porque es no supervisado)
kmeans.fit(X)
# Obtener los centros de los grupos y las etiquetas asignadas
centroides = kmeans.cluster_centers_
etiquetas = kmeans.labels_

print("Coordenadas de los centroides hallados:\n", centroides)
print("\nEtiquetas asignadas a los primeros 5 puntos:", etiquetas[:5])
