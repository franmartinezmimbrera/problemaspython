from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Cargar datos
iris = load_iris()
X = iris.data  # Características (largo de pétalo, ancho, etc.)
y = iris.target # Etiquetas (0, 1, 2 que representan las especies)

# Dividir en entrenamiento (80%) y prueba (20%)
# random_state=42 asegura que la división sea siempre la misma al ejecutar
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Total de datos: {X.shape[0]}")
print(f"Datos de entrenamiento: {X_train.shape[0]}")
print(f"Datos de prueba: {X_test.shape[0]}")y

