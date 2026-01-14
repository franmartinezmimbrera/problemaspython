import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Crear datos de ejemplo con una variable categórica
df = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia'],
    'Salario': [30000, 32000, 31000, 29000]
})

print("DataFrame Original ")
print(df)

# Inicializar el codificador
# sparse_output=False nos devuelve un array normal (numpy) en vez de una matriz dispersa
encoder = OneHotEncoder(sparse_output=False)

# Ajustar y transformar la columna 'Ciudad'
# Necesitamos pasarle un array 2D, por eso usamos las dobles corchetes [['Ciudad']]
ciudades_encoded = encoder.fit_transform(df[['Ciudad']])

# Ver el resultado y las categorías encontradas
print("\n Categorías detectadas ")
print(encoder.categories_)

print("\n Matriz One-Hot resultante ")
print(ciudades_encoded)
# Nota: La primera columna será 1 si es Barcelona, la segunda si es Madrid, etc.
