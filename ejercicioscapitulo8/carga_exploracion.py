import pandas as pd
from sklearn.datasets import load_iris

# Cargamos un dataset de ejemplo (Iris)
# Scikit-learn nos devuelve un objeto tipo diccionario, pero lo convertiremos
# a DataFrame de Pandas para que sea más legible, como un Excel.
datos_iris = load_iris()
df = pd.DataFrame(data=datos_iris.data, columns=datos_iris.feature_names)

# Añadimos la columna objetivo (target)
df['especie'] = datos_iris.target

# Mostramos las primeras 5 filas
print("Primeras 5 filas del dataset ")
print(df.head())

# Obtenemos información estadística básica
print("\n Descripción estadística del dataset")
print(df.describe())

# Verificamos tipos de datos y si hay nulos
print("\n Información del DataFrame ")
print(df.info())
