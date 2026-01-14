from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# Cargar datos
X, y = load_iris(return_X_y=True)

# Definir el modelo
# Usamos KNN (K-Vecinos más cercanos) como ejemplo

knn = KNeighborsClassifier(n_neighbors=5)
# Aplicar Validación Cruzada (Cross Validation) con 5 pliegues (folds)
# Esto divide los datos en 5 partes: entrena con 4 y prueba con 1, rotando 5 veces.
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
print("Puntuaciones en cada iteración:", scores)
print(f"Precisión media: {scores.mean():.2f}")
print(f"Desviación estándar: {scores.std():.2f}") 
# Una desviación baja indica que el modelo es estable.
