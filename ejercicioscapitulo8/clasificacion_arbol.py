from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Carga y Split
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo (Árbol de decisión)
# max_depth=3 limita la profundidad para evitar sobreajuste simple
arbol = DecisionTreeClassifier(max_depth=3, random_state=42)

# Entrenar
arbol.fit(X_train, y_train)

# Predecir sobre el conjunto de test
predicciones = arbol.predict(X_test)

print("Etiquetas reales (Test):   ", y_test[:10])
print("Etiquetas predichas:       ", predicciones[:10])
